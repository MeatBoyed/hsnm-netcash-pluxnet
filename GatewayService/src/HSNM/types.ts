import { z } from "zod";

export const HSNMPaymentParamsSchema = z.object({
  UseSandBox: z.number().int(), // If non-zero, uses test accounts
  GatewayID: z.number().int(), // ID of the hotspot gateway
  UsersID: z.number().int(), // ID of the user making the payment
  PaymentID: z.string().max(100), // Transaction ID
  PaymentType: z.string().max(20), // CustomPayment1 or CustomPayment2
  PaymentTypeDescr: z.string().max(255), // Payment type title
  TransactionType: z.number().int(), // Fixed value of 2
  Host: z.string().max(255), // URL of the HSNM Hotspot Manager
  ReturnURL: z.string().max(255), // URL to return to after payment
  IPNUrl: z.string().max(255), // Instant Payment Notification URL
  BackToWPText: z.string().max(255), // Text to return to Welcome Portal
  Lang: z.string().max(2), // Language code (ISO format)
  Recharge: z.number().int(), // 1 if payment is for a recharge
  ProductID: z.number().int(), // ID of the product being purchased
  ProductDescr: z.string().max(255), // Description of the product
  Currency: z.string().max(3), // Currency code (ISO 4217 format)
  Amount: z.number(), // Total amount including taxes
  Tax: z.number(), // VAT or other taxes
  Quantity: z.number().int().min(1).max(1), // Always 1
  FirstName: z.string().max(100), // First name of the user
  LastName: z.string().max(100), // Last name of the user
  Address: z.string().max(100), // User's address
  Zip: z.string().max(10), // ZIP code
  City: z.string().max(100), // City
  State: z.string().max(100), // State or province
  Country: z.string().max(100), // Country (ISO 3166-1 alpha-2)
  Email: z.string().email().max(50), // Email address
  Phone: z.string().max(20), // Phone number
});
export type HSNMPaymentParams = z.infer<typeof HSNMPaymentParamsSchema>;
