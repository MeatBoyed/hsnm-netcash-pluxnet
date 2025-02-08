from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class CreateInvoiceRequest(BaseModel):
    M1: str  # Merchant Service Key
    M2: str  # Software Vendor Code
    Amount: Decimal  # Invoice amount
    P2: str  # Unique reference for this invoice
    P3: str  # Invoice Description
    M9: Optional[str] = None  # Email of the person invoicing
    M4: Optional[str] = None  # Extra data field 1
    M5: Optional[str] = None  # Extra data field 2
    M6: Optional[str] = None  # Extra data field 3
    M10: Optional[str] = None  # Additional return string data
    IgnoreAmount: bool  # True: Call for amount to be paid, False: Use amount in barcode
    M11: Optional[str] = None  # Mobile number
    M12: bool  # Send SMS (M11 must contain valid data if true)
    M13: bool  # Send Email (M9 must contain valid data if true)
    M14: bool  # Request credit card token for subscriptions (default: False)
