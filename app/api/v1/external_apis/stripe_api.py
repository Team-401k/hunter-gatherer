from base_api import BaseApi
from dotenv import load_dotenv
import os                                                                                                                                                                                                          


import requests
import stripe
from datetime import datetime

load_dotenv()
stripe.api_key = os.getenv("Stripe_SECRET_KEY")


class StripeAPI(BaseApi):
    def __init__(self):
        super().__init__("https://api.stripe.com")
        self.headers = {
        }

    def search_transactions(self, start_date, end_date):
        try:
            # List charges for a specific customer and optionally within a certain time range
            # donations = stripe.
            # print(len(donations))
            charges = stripe.Charge.list(
                created = {
                    "gte": start_date,  # greater than or equal to this timestamp (start time)
                    "lt": end_date    # less than this timestamp (end time)

                }
            )

            # Iterate through the charges and do something with them
            for charge in charges.auto_paging_iter():
                # print(charge)
                print(f"Name: {charge['billing_details']['name']}, "
                    f"Amount: {charge['amount']}, "
                    f"Currency: {charge['currency']}, "
                    f"Date: {datetime.utcfromtimestamp(charge['created']).strftime('%Y-%m-%d %H:%M:%S')}, "
                    f"Application Fee: {charge.get('application_fee', 'N/A')}")
        except stripe.error.StripeError as e:
            # Handle error
            print(e)

    def get_donations(self, start_date, end_date):
        try:
            total_donations = []
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,
                    "lt": end_date
                }
            )

            for charge in charges.auto_paging_iter():
                if 'Donation' in charge.get('description'):
                    total_donations.append(charge)

            return total_donations
        except stripe.error.StripeError as e:
            print(e)
            return None


stripe_api = StripeAPI()
stripe_api.search_transactions(1707602577, 1708207377)

donations = stripe_api.get_donations(1672614308, 1704063908)

if donations:
    for donation in donations:
        print(f"Donation Transaction ID: {donation['id']}")
        print(f"Amount: {donation['amount'] / 100} {donation['currency']}")
        print(f"Description: {donation['description']}")
        print("-------------")
else:
    print("No donations found.")
