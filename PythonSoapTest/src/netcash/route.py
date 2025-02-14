from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

# from src.auth.dependencies import AccessTokenBearer
from src.netcash.service import NetCashService

netcash_router = APIRouter()
netcash_service = NetCashService()
# acccess_token_bearer = AccessTokenBearer()

@netcash_router.post("/pay")
def createPayment():
    # 1 -Validate Request source (Should only accept req from HSNM)

    # 2 - Validate All Inputs (Use the most Strict validation possible)

    # 3 - Make Payment Request 
    response = netcash_service.requestPayment(
        email='charles@mbvit.co.za',
        phone='0656853805',
        amount=100,
        reference='test reference'
    )

    # 4 - Error Handle Response with Respective HTTP Status Code
    return response
    # return 'hello'

# @netcash_router.post(
#         "/notify",
#         # status_code=status.HTTP_201_CREATED,
#         # response_model=Book,
#         # dependencies=[role_checker],
# )
# async def createPayment() -> str:
#     # 1 -Validate Request source (Should only accept req from HSNM)

#     # 2 - Validate All Inputs (Use the most Strict validation possible)

#     # 3 - Relay Response to HSNM success
#     # 4 - Error Handle Response with Respective HTTP Status Code
#     return ''

# response = soap.service.CreateInvoice(
#     NETCASH_SERVICE_KEY,
#     NETCASH_SOFTWARE_VENDOR_KEY,
#     100,
#     "Test payment"
#     , "Test payment request",
#     "stephan.botes@bottomlineit.co.za",
#     "", "", "", "", True, "0656853805", True, True, False)