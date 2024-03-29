# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.balances_response import BalancesResponse

class TestBalancesResponse(unittest.TestCase):
    """BalancesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BalancesResponse:
        """Test BalancesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BalancesResponse`
        """
        model = BalancesResponse()
        if include_optional:
            return BalancesResponse(
                balances = [
                    openapi_client.models.balance_information.Balance Information(
                        currency = '012', 
                        primary = True, 
                        total_balance = openapi_client.models.money.Money(
                            currency_code = '012', 
                            value = '-.2888001528021798096225500850', ), 
                        available_balance = openapi_client.models.money.Money(
                            currency_code = '012', 
                            value = '-.2888001528021798096225500850', ), 
                        withheld_balance = , )
                    ],
                account_id = 'RZ87D9HDX393Z0123456789101112',
                as_of_time = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819',
                last_refresh_time = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819'
            )
        else:
            return BalancesResponse(
        )
        """

    def testBalancesResponse(self):
        """Test BalancesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
