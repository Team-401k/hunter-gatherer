from app.api.v1.external_apis.base_api import BaseApi
import os
from dotenv import load_dotenv

load_dotenv()

class SquareSpaceAPI(BaseApi):
    def __init__(self):
        api_key = os.getenv('SQUARESPACE_API_KEY')
        print("API KEY IS", api_key)
        # api_key = "fd12f7c1-ccd1-489d-adc5-164687c4791b"
        super().__init__('https://api.squarespace.com') 
        self.api_key = api_key

    def make_request(self, url: str, method: str, headers: dict = None, params: dict = None, data: dict = None) -> dict:
        if headers is None:
            headers = {}
        # Add the Authorization header with your SquareSpace API key
        headers['Authorization'] = f'Bearer {self.api_key}'
        # Proceed with the request as usual
        return super().make_request(url, method, headers, params, data)
    
    def get_orders(self, modifiedAfter=None, modifiedBefore=None, cursor=None, fulfillmentStatus=None):
        # Prepare the request parameters
        params = {}
        if modifiedAfter:
            params['modifiedAfter'] = modifiedAfter
        if modifiedBefore:
            params['modifiedBefore'] = modifiedBefore
        if cursor:
            params['cursor'] = cursor
        if fulfillmentStatus:
            params['fulfillmentStatus'] = fulfillmentStatus

        # Make the request to the SquareSpace orders endpoint
        response = self.make_request('/1.0/commerce/orders', 'GET', params=params)
        return response
    
squareSpaceAPI = SquareSpaceAPI()
orders = squareSpaceAPI.get_orders(modifiedAfter='2024-02-10T00:00:00Z', modifiedBefore='2024-02-17T23:59:59Z')
print(orders)   