import { NetCashPaymentSchema, type NetCashPayment } from "./types.js";

// Function to send payment request
export async function makePaymentRequest(paymentData: NetCashPayment): Promise<void> {
  try {
    // Validate the input data using Zod
    const validatedData = NetCashPaymentSchema.parse(paymentData);

    // Make the POST request using Fetch API
    const response = await fetch("https://paynow.netcash.co.za/site/paynow.aspx", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded", // Form submission mimicking
      },
    // Since NetCash is providing a form-based example, 
    // they most likely expect data in URL-encoded format (application/x-www-form-urlencoded). 🚀
      body: new URLSearchParams(validatedData).toString(), // Convert JSON to form-urlencoded
    });

    // Check response status
    if (!response.ok) {
      throw new Error(`Request failed with status: ${response.status}`);
    }

    // Handle response (NetCash may redirect)
    const result = await response.text();
    console.log("Payment Response:", result);
  } catch (error) {
    console.error("Error processing payment:", error);
  }
}