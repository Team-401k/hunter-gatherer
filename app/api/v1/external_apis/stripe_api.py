import os
import time
from datetime import datetime

import stripe
from dotenv import load_dotenv

from app.api.v1.external_apis.base_api import BaseApi
from app.api.v1.external_apis.schemas import ChargesResponse


def iso_to_unix(timestamp):
    """Convert ISO 8601 string to UNIX timestamp."""
    # Convert the ISO 8601 string to a datetime object
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    # Convert the datetime object to UNIX timestamp and return it
    return int(time.mktime(dt.timetuple()))


class StripeAPI(BaseApi):
    def __init__(self):
        super().__init__("https://api.stripe.com")
        self.headers = {}
        load_dotenv()
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def search_transactions(self, start_date_orig, end_date_orig):
        start_date = iso_to_unix(start_date_orig)
        end_date = iso_to_unix(end_date_orig)
        try:
            # List charges for a specific customer and optionally within a certain time range
            # donations = stripe.
            # print(len(donations))
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,  # greater than or equal to this timestamp (start time)
                    "lte": end_date,  # less than this timestamp (end time)
                },
            )
            return charges

            # # Iterate through the charges and do something with them
            # for charge in charges.auto_paging_iter():
            #     # print(charge)
            #     print(f"Name: {charge['billing_details']['name']}, "
            #         f"Amount: {charge['amount']}, "
            #         f"Currency: {charge['currency']}, "
            #         f"Date: {datetime.utcfromtimestamp(charge['created']).strftime('%Y-%m-%d %H:%M:%S')}, "
            #         f"Application Fee: {charge.get('application_fee', 'N/A')}")
        except stripe.error.StripeError as e:
            # Handle error
            print(e)

    def parse(self, charges):
        return ChargesResponse(**charges)

    def search_parse(self, start_date, end_date):
        charges = self.search_transactions(start_date, end_date)
        return self.parse(charges)

    def get_donations(self, start_date, end_date):
        try:
            total_donations = []
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,
                    "lt": end_date,
                },
            )

            for charge in charges.auto_paging_iter():
                if "Donation" in charge.get("description"):
                    total_donations.append(charge)

            return total_donations
        except stripe.error.StripeError as e:
            print(e)
            return None


# Example Call
# stripe_api = StripeAPI()
# charges = stripe_api.search_parse('2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')

# # Now you can access the parsed data
# for charge in charges.data:
#     print(charge.amount)

# donations = stripe_api.get_donations(1672614308, 1704063908)

# if donations:
#     for donation in donations:
#         print(f"Donation Transaction ID: {donation['id']}")
#         print(f"Amount: {donation['amount'] / 100} {donation['currency']}")
#         print(f"Description: {donation['description']}")
#         print("-------------")
# else:
#     print("No donations found.")
