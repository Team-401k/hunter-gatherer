# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.balances_api import BalancesApi


class TestBalancesApi(unittest.TestCase):
    """BalancesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BalancesApi()

    def tearDown(self) -> None:
        pass

    def test_balances_get(self) -> None:
        """Test case for balances_get

        List all balances
        """
        pass


if __name__ == '__main__':
    unittest.main()
