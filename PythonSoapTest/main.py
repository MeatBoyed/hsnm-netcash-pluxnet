from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

# SOAP Library
from zeep import Client;
from models import CreateInvoiceRequest
from utils import extract_payment_url

# WSDL URL
WSDL_URL = 'https://ws.sagepay.co.za/Paynow/PayNow.svc?singleWsdl' # ADD TO ENVIRONMENT VARIABLES
NETCASH_URL = 'https://ws.sagepay.co.za/PayNow/PayNow.svc' # ADD TO ENVIRONMENT VARIABLES

NETCASH_SERVICE_KEY= "70b4a01f-e7da-4c62-a9f6-4a7f61ef84ea"
NETCASH_SOFTWARE_VENDOR_KEY="24ade73c-98cf-47b3-99be-cc7b867b3080"

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/paynow")
def create_invoice(amount: float, email: str, phone: str, reference: str):
    # Validate Request source (Should only accept req from HSNM)

    # Validate All Inputs (Use the most Strict validation possible)

    soapClient = Client(WSDL_URL)
    # Create Invoice Request
    response_xml = soapClient.service.CreateInvoice(
        NETCASH_SERVICE_KEY,  # M1
        NETCASH_SOFTWARE_VENDOR_KEY,  # M2
        amount,              # Amount
        reference,           # P2 (Unique reference)
        "Test Payment Request form MBV FastAPI",   # P3 (Description)
        email,               # M9 (Email)
        "", "", "", "",      # M4, M5, M6, M10 (Extra fields)
        True,                # IgnoreAmount
        phone,               # M11 (Mobile number)
        True,                # M12 (Send SMS)
        True,                # M13 (Send Email)
        False                # M14 (Request credit card token)
    )
      
    # Extract the payment URL using the helper function
    payment_url = extract_payment_url(response_xml)

    if payment_url:
        return RedirectResponse(url=payment_url)
        # return {"payment_url": payment_url}
    return {"error": "Payment URL not found"}

# Netcash notification
# Field No:	Field Name:	Alpha / Numeric / Boolean	Description:
# 1	TransactionAccepted	B	“true” means the transaction was successful
# 2	CardHolderIpAddr	AN	This is the original IP the request was made from
# 3	RequestTrace	AN	This is a unique trace id for the transaction. This id can be used to retrieve additional information from the 3rd Party transaction logs
# 4	Reference	AN	The unique reference sent to Netcash in the original request
# 5	Extra1	AN	The extra field sent in the m4 variable when you made the reques
# 6	Extra2	AN	The extra field sent in the m5 variable when you made the request
# 7	Extra3	AN	The extra field sent up in the m6 variable when you made the request
# 8	Amount	N	This is the amount sent Netcash in the original request
# 9	Method	N	1 Credit card
# 2 Bank EFT
# 3 Retail
# 4 Ozow
# 5 MasterPass
# 6 Visa Checkout
# 7 Masterpass QR
# 8 Mobicred
# 9 Payflex
# 10 Flash1Voucher
# The below four (4) fields are only returned if:

# The transaction was a Credit Card payment
# M14 (tokenise card) field is set to True
# “Test Mode” in the NetConnector Profile in the Netcash Account is set to false
# 10	ccToken	AN	Credit Card Vault GUiD
# 11	ccHolder	AN	Credit Cardholder name
# 12	ccMasked	AN	Masked Credit Card number
# 13	ccExpiry	N	Credit Card expiry date MMCCYY

# Send info to HSNM

@app.get("/notify")
def create_invoice(amount: float, email: str, phone: str, reference: str):
    # Validate Request source (Should only accept req from HSNM)

    # Validate All Inputs (Use the most Strict validation possible)

    
      
    # Extract the payment URL using the helper function
    payment_url = extract_payment_url(response_xml)

    if payment_url:
        return RedirectResponse(url=payment_url)
        # return {"payment_url": payment_url}
    return {"error": "Payment URL not found"}