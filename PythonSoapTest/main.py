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
    soapClient = Client(WSDL_URL)
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


    # Create Invoice Request
    # invoice_data = CreateInvoiceRequest(
    #     M1="70b4a01f-e7da-4c62-a9f6-4a7f61ef84ea",
    #     M2="24ade73c-98cf-47b3-99be-cc7b867b3080",
    #     Amount=10.00,
    #     P2="12345",
    #     P3="Test Request from Python",
    #     M9="charles@mbvit.co.za",
    #     IgnoreAmount=True,
    #     M11="0837072977",
    #     M12=True,
    #     M13=True,
    #     M14=False
    # ) 
    # invoice_dict = invoice_data.dict()
    # response = soapClient.service.CreateInvoice(**invoice_dict)
