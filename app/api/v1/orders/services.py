"""Services for orders."""

import enum
from app.api.v1.external_apis.pp_api import PayPalAPI
from app.api.v1.external_apis.schemas import OrdersResponse
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI
from app.api.v1.external_apis.stripe_api import StripeAPI


paypal_api = PayPalAPI()
stripe_api = StripeAPI()
sqsp_api = SquareSpaceAPI()

class OrderService(str, enum.Enum):
    PAYPAL = 'paypal'
    STRIPE = 'stripe'
    SQSP = 'sqsp'


def get_orders(origin: OrderService, start_date: str, end_date: str) -> OrdersResponse:
    # First get the parsed orders from paypal
    # if origin == OrderService.PAYPAL:
    #     return paypal_api.search_parse(start_date, end_date)
    # elif origin == OrderService.STRIPE:
    #     return (stripe_api.search_parse(start_date, end_date)).data
    # elif origin == OrderService.SQSP:
    return sqsp_api.search_parse_orders(start_date, end_date)