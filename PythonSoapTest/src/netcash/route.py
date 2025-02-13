from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

# from src.auth.dependencies import AccessTokenBearer
from src.netcash.service import NetCashService

netcash_router = APIRouter()
netcash_service = NetCashService()
# acccess_token_bearer = AccessTokenBearer()

@netcash_router.get(
        "/",
        status_code=status.HTTP_201_CREATED,
        # response_model=Book,
        # dependencies=[role_checker],
)
async def createPayment() -> str:
    # 1 -Validate Request source (Should only accept req from HSNM)

    # 2 - Validate All Inputs (Use the most Strict validation possible)

    # 3 - Make Payment Request 
    # response_url = await netcash_service.requestPayment(
    #     email='',
    #     phone='',
    #     amount=10,
    #     reference=''
    # )

    # 4 - Error Handle Response with Respective HTTP Status Code

    # return RedirectResponse(url=response_url)
    return 'hello'

@netcash_router.post(
        "/notify",
        # status_code=status.HTTP_201_CREATED,
        # response_model=Book,
        # dependencies=[role_checker],
)
async def createPayment() -> str:
    # 1 -Validate Request source (Should only accept req from HSNM)

    # 2 - Validate All Inputs (Use the most Strict validation possible)

    # 3 - Relay Response to HSNM success
    # 4 - Error Handle Response with Respective HTTP Status Code
    return ''

