import os

from dotenv import load_dotenv

from app.api.v1.external_apis.base_api import BaseApi
from app.api.v1.external_apis.schemas import (
    OrdersResponse,
    SqspOrderDetailResponse,
    SqspProductResponse,
    SqspProfileResponse,
    SqspTransactionsResponse,
)


class SquareSpaceAPI(BaseApi):

    def __init__(self):
        load_dotenv()  # load the .env
        api_key = os.getenv("SQUARESPACE_API_KEY")
        super().__init__("https://api.squarespace.com")
        self.api_key = api_key

    def make_request(
        self,
        url: str,
        method: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
    ) -> dict:
        if headers is None:
            headers = {}
        # Add the Authorization header with your SquareSpace API key
        headers["Authorization"] = f"Bearer {self.api_key}"
        # Proceed with the request as usual
        return super().make_request(url, method, headers, params, data)

    def get_orders_list(
        self,
        modifiedAfter=None,
        modifiedBefore=None,
        cursor=None,
        fulfillmentStatus=None,
    ):
        # Prepare the request parameters
        params = {}
        if modifiedAfter:
            params["modifiedAfter"] = modifiedAfter
        if modifiedBefore:
            params["modifiedBefore"] = modifiedBefore
        if cursor:
            params["cursor"] = cursor
        if fulfillmentStatus:
            params["fulfillmentStatus"] = fulfillmentStatus

        # Make the request to the SquareSpace orders endpoint
        response = self.make_request("/1.0/commerce/orders", "GET", params=params)
        return response

    def get_order_detail(self, order_id):
        # Make the request to the SquareSpace orders endpoint
        print("ahh this is prob the issue huh", order_id)
        response = self.make_request(f"/1.0/commerce/orders/{order_id}", "GET")
        print("was this is eht issue?", response)
        return response

    def get_transactions(
        self,
        modifiedAfter=None,
        modifiedBefore=None,
        cursor=None,
        fulfillmentStatus=None,
    ):
        # Prepare the request parameters
        params = {}
        if modifiedAfter:
            params["modifiedAfter"] = modifiedAfter
        if modifiedBefore:
            params["modifiedBefore"] = modifiedBefore
        if cursor:
            params["cursor"] = cursor
        if fulfillmentStatus:
            params["fulfillmentStatus"] = fulfillmentStatus

        # Make the request to the SquareSpace orders endpoint
        response = self.make_request("/1.0/commerce/transactions", "GET", params=params)
        return response

    def get_products(self, cursor: str = None):
        # Prepare the request parameters
        params = {}
        if cursor:
            params["cursor"] = cursor

        # Make the request to the SquareSpace inventory endpoint
        response = self.make_request("/1.0/commerce/inventory", "GET", params=params)
        return response

    def get_profile(self, email: str):
        # Prepare the request parameters
        params = {}
        if email:
            params["filter"] = f"email,{email}"

        # Make the request to the SquareSpace inventory endpoint
        response = self.make_request("/1.0/profiles", "GET", params=params)
        return response

    def parse_orders_list(self, data) -> OrdersResponse:
        return OrdersResponse.model_validate(data)

    def parse_order_detail(self, data) -> SqspOrderDetailResponse:
        return SqspOrderDetailResponse.model_validate(data)

    def parse_transactions(self, data):
        return SqspTransactionsResponse.model_validate(data)

    def parse_products(self, data):
        products = SqspProductResponse.model_validate(data)
        return products

    def parse_profiles(self, data):
        profiles = SqspProfileResponse.model_validate(data)
        return profiles

    def search_parse_orders_list(
        self,
        modifiedAfter=None,
        modifiedBefore=None,
        cursor=None,
        fulfillmentStatus=None,
    ) -> OrdersResponse:
        data = self.get_orders_list(
            modifiedAfter,
            modifiedBefore,
            cursor,
            fulfillmentStatus,
        )
        return self.parse_orders_list(data)

    def search_parse_transactions(
        self,
        modifiedAfter=None,
        modifiedBefore=None,
        cursor=None,
        fulfillmentStatus=None,
    ) -> SqspTransactionsResponse:
        data = self.get_transactions(
            modifiedAfter,
            modifiedBefore,
            cursor,
            fulfillmentStatus,
        )
        return self.parse_transactions(data)

    def search_parse_products(self, cursor=None) -> SqspProductResponse:
        data = self.get_products(cursor)
        return self.parse_products(data)

    def search_parse_order_detail(self, order_id) -> SqspOrderDetailResponse:
        print("begin search parse order detail", order_id)
        data = self.get_order_detail(order_id)
        print("in search parse order detail", data)
        return self.parse_order_detail(data)

    def search_parse_profile(self, email) -> SqspProfileResponse:
        data = self.get_profile(email)
        return self.parse_profiles(data)


# Define the order class
# class Order:
#     def __init__(self, id, order_number, created_on, modified_on, customer_email, billing_address, line_items, total):
#         self.id = id
#         self.order_number = order_number
#         self.created_on = created_on
#         self.modified_on = modified_on
#         self.customer_email = customer_email
#         self.billing_address = billing_address
#         self.line_items = line_items
#         self.total = total

#     def __str__(self):
#         return f"Order Number: {self.order_number}, Email: {self.customer_email}, Total: {self.total['value']} {self.total['currency']}"

# def create_order_instances(api_data):
#     orders = []
#     for order_data in api_data.get('result', []):
#         # Create a dictionary with the data for the new Order
#         new_order_data = {
#             'member_id': None,  # You need to determine the member_id based on your application logic
#             'amount': float(order_data['grandTotal']['value']),
#             'date': current_utc_time(),
#             'type': 'forum',  # You need to determine the type based on your application logic
#             'method': 'stripe',  # Assume 'stripe' for this example, adjust as needed
#             'fee': 0.0,  # Set a default fee or calculate as required
#             'stripe_paypal_id': None  # You need to extract this from your payment gateway data
#         }

#         # Append a new Order instance to the list
#         orders.append(Order(**new_order_data))
#     return orders

# #Example Call\
# orders_response = squareSpaceAPI.search_parse('2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')

# # Now access orders as Pydantic models
# for order in orders_response.result:
#     print(order.id)
# print(data)

# # Pydantic OrderWrapper to unwrap API call into

# order_wrapper = OrderWrapper.model_validate(data)
# for order in order_wrapper.result:
#     created_on_str = order.createdOn.strftime('%Y-%m-%d %H:%M:%S') if order.createdOn else None
#     modified_on_str = order.modifiedOn.strftime('%Y-%m-%d %H:%M:%S') if order.modifiedOn else None
#     print(order)
#     order = Order(
#         id=order.id,
#         orderNumber=order.orderNumber,
#         total=order.grandTotal.value,
#         createdOn=created_on_str,
#         modifiedOn=modified_on_str,
#         customerEmail=order.customerEmail,
#         billingAddress=f"{order.billingAddress.address1}, {order.billingAddress.address2}" if order.billingAddress.address2 else order.billingAddress.address1
#     )
#     print("Order is ", order)
# =======
# orders = squareSpaceAPI.get_orders(modifiedAfter='2023-12-10T00:00:00Z', modifiedBefore='2024-02-17T23:59:59Z')
# print(orders)
