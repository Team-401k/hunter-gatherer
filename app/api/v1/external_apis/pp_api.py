from base_api import BaseApi
from dotenv import load_dotenv
import os

import requests

load_dotenv()
class PayPalAPI(BaseApi):
    def __init__(self, client_id, client_secret):
        super().__init__("https://api-m.paypal.com")
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {
        }

    def get_oauth_token(self):
        auth_data = {"grant_type": "client_credentials"}
        auth_response = requests.post(self.base_url + "/v1/oauth2/token", auth=(self.client_id, self.client_secret),
                                      data=auth_data, headers=self.headers)
        json = auth_response.json()
        print(json)
        print()
        if auth_response.status_code == 200:
            self.headers['Authorization'] = "Bearer " + json['access_token']
        else:
            auth_response.raise_for_status()

    def search_transactions(self, start_date: str, end_date: str, transaction_type: str = None):
        # do this every time
        self.get_oauth_token()
        params = {"start_date": start_date, "end_date": end_date}
        if transaction_type:
            params['transaction_type'] = transaction_type
        # mak sure to only put in non base part of the url when call make_request
        return self.make_request("/v1/reporting/transactions", "GET", headers=self.headers, params=params)

    def get_donations(self, start_date: str, end_date: str):
        self.get_oauth_token()
        total_transactions = self.search_transactions(start_date, end_date)
        if total_transactions:
            donation_orders = [transaction for transaction in total_transactions['transaction_details'] if
                               'transaction_info' in transaction and
                               'transaction_subject' in transaction['transaction_info'] and
                               'Donation' in transaction['transaction_info']['transaction_subject']]

            return donation_orders
        else:
            print("Error retrieving transactions.")
            return None


# Example call
client_id = os.getenv("PayPal_CLIENT_ID")
secret_key = os.getenv("PayPal_SECRET_KEY")
paypal_api = PayPalAPI(client_id, secret_key)
transactions = paypal_api.search_transactions('2023-10-01T00:00:00-0700', '2023-10-31T00:00:00-0700')
donations = paypal_api.get_donations('2023-12-01T00:00:00-0700', '2023-12-30T00:00:00-0700')
print(donations)
print(transactions['transaction_details'])
