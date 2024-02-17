from base_api import BaseApi

import requests
import stripe

stripe.api_key = "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"


class StripeAPI(BaseApi):
    def __init__(self):
        super().__init__("https://api.stripe.com")
        self.headers = {
        }
    
    def search_transactions(self, start_date, end_date):
        try:
            # List charges for a specific customer and optionally within a certain time range
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,  # timestamp for one week ago
                    "lt": end_date    # timestamp for now (feb 17th 2023 2:10:00)
                }
            )
            
            # Iterate through the charges and do something with them
            for charge in charges.auto_paging_iter():
                print(charge)
        except stripe.error.StripeError as e:
            # Handle error
            print(e)


stripe_api = StripeAPI()
stripe_api.search_transactions(1707602577, 1708207377)