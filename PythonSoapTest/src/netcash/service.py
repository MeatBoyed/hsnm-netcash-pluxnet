from zeep import Client;
from datetime import datetime
from src.config import Config
from src.utils.xaml_extractor import extract_payment_url

class NetCashService:
    Client = Client(Config.WSDL_URL) # SOAP Client

    # Execute Payment/Invoice Request via SOAP
    async def requestPayment(self, email:str, phone:str, amount: float, reference: str):
        # 1 - Make Request 
        response_xml = self.Client.service.CreateInvoice(
            Config.NETCASH_SERVICE_KEY,  # M1
            Config.NETCASH_SOFTWARE_VENDOR_KEY,  # M2
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

        # 2 - Extract the Payment_URL from response
        payment_url = extract_payment_url(response_xml)

        if payment_url:
            return payment_url
        else:
            return
    