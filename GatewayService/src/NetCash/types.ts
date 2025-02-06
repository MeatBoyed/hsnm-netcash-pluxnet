import { z } from "zod";


// NetCash Payment Request Data Schema
export const NetCashPaymentSchema = z.object({
  M1: z.string().uuid(),  // Pay Now Service Key
  M2: z.string().uuid(),  // Software Vendor Key
  p2: z.string(),         // Unique transaction ID
  p3: z.string(),         // Description of goods
  p4: z.string(),         // Amount (string to maintain precision)
  Budget: z.literal("Y"), // Budget field (must be "Y")
  m4: z.string().optional(), // Extra field 1
  m5: z.string().optional(), // Extra field 2
  m6: z.string().optional(), // Extra field 3
  m9: z.string().email(),    // Cardholder's email
  m10: z.string(),           // Shopping cart dataset
  m11: z.string(),           // Cardholder's mobile number
  m14: z.enum(["0", "1"]),   // Request credit card subscription token
  m15: z.string().uuid().optional(), // Credit card token (optional)
});
export type NetCashPayment = z.infer<typeof NetCashPaymentSchema>;