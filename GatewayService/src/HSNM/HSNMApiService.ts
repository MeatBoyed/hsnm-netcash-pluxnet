import crypto from "crypto";

export class HSNMApiService {
  private baseUri: string;
  private apiKey: string;
  private apiSecret: string;
  private secretIV: Buffer;

  constructor(domainOrIP: string, key: string, secret: string) {
    this.baseUri = `${domainOrIP}/api/v2/`;
    this.apiKey = key;
    this.apiSecret = secret;

    // Encryption vector initialization (first 16 bytes of SHA-256 hash of the API key)
    this.secretIV = crypto.createHash("sha256").update(this.apiKey).digest().subarray(0, 16);
  }

  // Base64 URL Encoding (PHP equivalent)
  private base64UrlEncode(data: Buffer): string {
    return data.toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  }

  // Encrypt Data using AES-256-CBC
  private encryptData(data: string): string {
    const cipher = crypto.createCipheriv("aes-256-cbc", crypto.createHash("md5").update(this.apiSecret).digest(), this.secretIV);
    const encrypted = Buffer.concat([cipher.update(data, "utf8"), cipher.final()]);
    return this.base64UrlEncode(encrypted);
  }

  // API Call function
  async apiCall(endpoint: string, data: object): Promise<any> {
    try {
      const encryptedData = this.encryptData(JSON.stringify(data));

      const response = await fetch(`${this.baseUri}${endpoint}/apikey=${this.apiKey}`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ data: encryptedData }).toString(),
      });

      if (!response.ok) throw new Error(`Request failed with status: ${response.status}`);

      return await response.json();
    } catch (error) {
      console.error("API Error:", error);
      return { warning: "", error: "Generic error" };
    }
  }
}

// Example Usage
// const hsnmApi = new HSNMApiService("https://your-hsnm-domain.com", "your-api-key", "your-api-secret");

// (async () => {
//   const result = await hsnmApi.apiCall("example-endpoint", { test: "data" });
//   console.log(result);
// })();
