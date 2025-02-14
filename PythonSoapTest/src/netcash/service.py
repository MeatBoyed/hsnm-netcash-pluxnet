from zeep import Client;
from datetime import datetime
from src.config import Config
from fastapi import FastAPI, HTTPException
from src.utils.xaml_extractor import extract_payment_url

class NetCashService:

    # Execute Payment/Invoice Request via SOAP
    def requestPayment(self, email:str, phone:str, amount: float, reference: str):
        try:
            soapClient = Client(Config.WSDL_URL) # SOAP Client
        except Exception as soapErr:
            print("SOAP Exception: ", soapErr)
            raise HTTPException(status_code=500, detail="An exception occurred when generating the SOAP Client")
        
        # 1 - Make Request 
        netCashResponse = soapClient.service.CreateInvoice(
            Config.NETCASH_SERVICE_KEY,  # M1
            Config.NETCASH_SOFTWARE_VENDOR_KEY,  # M2
            amount,              # Amount
            reference,           # P2 (Unique reference)
            "Test Payment Request form MBV FastAPI",   # P3 (Description)
            email,               # M9 (Email)
            "", "", "", "",      # M4, M5, M6, M10 (Extra fields)
            True,                # IgnoreAmoun
            phone,               # M11 (Mobile number)
            True,                # M12 (Send SMS)
            True,                # M13 (Send Email)
            False                # M14 (Request credit card token)
        )

        # Check & Log NetCash response
        print(netCashResponse)
        if (netCashResponse == '100'):
            return 'Authentication failed'
        elif (netCashResponse == '103'):
            return 'Invalid Keys'
        elif(netCashResponse == '200'):
            return 'Web Service error'
        elif(netCashResponse == '301'):
            return 'Reference not unique'
        elif(netCashResponse == '310'):
            return 'Request not activated for this'


        # print(soapClient.service.CreateInvoice)

        # 2 - Extract the Payment_URL from response
        try:
            payment_url = extract_payment_url(netCashResponse)
        except Exception as extractError:
            print("XAML Parsing Error: ", extractError)
            raise HTTPException(status_code=500, detail="An exception occured when Parsing Response")


        if payment_url:
            return payment_url
        else:
            return 'Failed R'
    