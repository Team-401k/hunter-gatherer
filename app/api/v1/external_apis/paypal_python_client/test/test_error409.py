# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.error409 import Error409

class TestError409(unittest.TestCase):
    """Error409 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Error409:
        """Test Error409
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Error409`
        """
        model = Error409()
        if include_optional:
            return Error409(
                name = 'RESOURCE_CONFLICT',
                message = 'The server has detected a conflict while processing this request.',
                details = [
                    openapi_client.models.error_details.Error Details(
                        field = '', 
                        value = '', 
                        location = 'body', 
                        issue = '', 
                        description = '', )
                    ],
                debug_id = '',
                links = [
                    openapi_client.models.link_description.Link Description(
                        href = '', 
                        rel = '', 
                        method = 'GET', )
                    ]
            )
        else:
            return Error409(
        )
        """

    def testError409(self):
        """Test Error409"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
