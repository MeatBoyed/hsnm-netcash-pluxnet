from fastapi import FastAPI
from src.error import register_all_errors
from src.middleware import register_middleware
from src.config import Config

# Routes
from src.netcash.route import netcash_router

version = "v1"

description = """
A REST API for PluxNet's HSNM & NetCash Integration Web Service.

This REST API is able to;
- Review Customer generated Payment Requests from HSNM
- Create Payment Request to Customers from NetChash
- Listen to NetCash Transaction Notifications
- Notify HSNM of Notified Transactions
"""

version_prefix =f"/api/{version}"

app = FastAPI(
    title="HSNM-to-NetCash",
    description=description,
    version=version,
    # license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Charles Rossouw",
        "url": "https://github.com/meatboyed",
        "email": "charles@mbvit.co.za",
    },
    terms_of_service=f"httpS://{Config.APP_DOMAIN}/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)

register_middleware(app)

# Register Route Handlers
app.include_router(netcash_router, prefix=f"{version_prefix}/netcash", tags=["netcash"])