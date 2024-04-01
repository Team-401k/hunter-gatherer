"""Services for orders."""

import enum
from app.api.v1.external_apis.pp_api import PayPalAPI
from app.api.v1.external_apis.schemas import OrdersResponse, SqspOrderDetailResponse, SqspTransactionsResponse
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI
from app.api.v1.external_apis.stripe_api import StripeAPI


paypal_api = PayPalAPI()
stripe_api = StripeAPI()
sqsp_api = SquareSpaceAPI()

class OrderService(str, enum.Enum):
    PAYPAL = 'paypal'
    STRIPE = 'stripe'
    SQSP = 'sqsp'


def get_orders(start_date: str, end_date: str) -> OrdersResponse:
    # First get the parsed orders from paypal
    # if origin == OrderService.PAYPAL:
    #     return paypal_api.search_parse(start_date, end_date)
    # elif origin == OrderService.STRIPE:
    #     return (stripe_api.search_parse(start_date, end_date)).data
    # elif origin == OrderService.SQSP:
    return sqsp_api.search_parse_orders_list(start_date, end_date)

def get_order_detail(order_id: str) -> SqspOrderDetailResponse:
    return sqsp_api.get_order_detail(order_id)

def get_transactions(start_date: str, end_date: str) -> SqspTransactionsResponse:
    return sqsp_api.search_parse_transactions(start_date, end_date)

def parse_forum_customizations(customizations):
    first_name = ""
    last_name = ""
    phone = ""
    email = ""
    for customization in customizations:
        if customization.label == "First Name":
            first_name = customization.value if customization.value else ""
        elif customization.label == "Last Name":
            last_name = customization.value if customization.value else ""
        elif customization.label == "Phone":
            phone = customization.value if customization.value else ""
        elif customization.label == "Email":
            email = customization.value if customization.value else ""
    return first_name, last_name, phone, email

def parse_membership_customizations(customizations):
    address_line = ""
    city = ""
    state = ""
    postal_code = ""
    phone = ""
    name = ""
    email = ""
    emergency_contact = ""
    emergency_contact_phone = ""
    for customization in customizations:
        if customization.label == "Address":
            address_line = customization.value if customization.value else ""
        elif customization.label == "City":
            city = customization.value if customization.value else ""
        elif customization.label == "State":
            state = customization.value if customization.value else ""
        elif customization.label == "Postal Code":
            postal_code = customization.value if customization.value else ""
        elif customization.label == "Phone":
            phone = customization.value if customization.value else ""
        elif customization.label == "Name":
            name = customization.value if customization.value else ""
        elif customization.label == "Email":
            email = customization.value if customization.value else ""
        elif customization.label == "Emergency Contact Name":
            emergency_contact = customization.value if customization.value else ""
        elif customization.label == "Emergency Contact Phone":
            emergency_contact_phone = customization.value if customization.value else ""
    
    return address_line, city, state, postal_code, phone, name, email, emergency_contact, emergency_contact_phone