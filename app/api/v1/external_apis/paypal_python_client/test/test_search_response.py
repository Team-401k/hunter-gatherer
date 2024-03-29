# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.search_response import SearchResponse

class TestSearchResponse(unittest.TestCase):
    """SearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchResponse:
        """Test SearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchResponse`
        """
        model = SearchResponse()
        if include_optional:
            return SearchResponse(
                transaction_details = [
                    openapi_client.models.transaction_details.Transaction Details(
                        transaction_info = openapi_client.models.transaction_information.Transaction Information(
                            paypal_account_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            transaction_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            paypal_reference_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            paypal_reference_id_type = 'ODR', 
                            transaction_event_code = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            transaction_initiation_date = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819', 
                            transaction_updated_date = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819', 
                            transaction_amount = openapi_client.models.money.Money(
                                currency_code = '012', 
                                value = '-.2888001528021798096225500850', ), 
                            fee_amount = openapi_client.models.money.Money(
                                currency_code = '012', 
                                value = '-.2888001528021798096225500850', ), 
                            discount_amount = , 
                            insurance_amount = , 
                            sales_tax_amount = , 
                            shipping_amount = , 
                            shipping_discount_amount = , 
                            shipping_tax_amount = , 
                            other_amount = , 
                            tip_amount = , 
                            transaction_status = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            transaction_subject = '5''UOq1hlK5jZXw'V6.YZb0', 
                            transaction_note = '5''UOq1hlK5jZXw'V6.YZb0', 
                            payment_tracking_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            bank_reference_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            ending_balance = , 
                            available_balance = , 
                            invoice_id = '5''UOq1hlK5jZXw'V6.YZb0', 
                            custom_field = '5''UOq1hlK5jZXw'V6.YZb0', 
                            protection_eligibility = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            credit_term = 'GqWzyBAw2ZuufUOHOEhA8I0', 
                            credit_transactional_fee = , 
                            credit_promotional_fee = , 
                            annual_percentage_rate = '-.2888001528021798096225500850', 
                            payment_method_type = 'GqWzyBAw2ZuufUOHOEhA8I0', 
                            instrument_type = '0', 
                            instrument_sub_type = '0', ), 
                        payer_info = openapi_client.models.payer_information.Payer Information(
                            account_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            email_address = 'j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG012', 
                            phone_number = openapi_client.models.phone.Phone(
                                country_code = '8070', 
                                national_number = '807288800150', 
                                extension_number = '8072888001528020', ), 
                            address_status = '|0', 
                            payer_status = '|0', 
                            payer_name = openapi_client.models.name.Name(
                                prefix = '', 
                                given_name = '', 
                                surname = '', 
                                middle_name = '', 
                                suffix = '', 
                                alternate_full_name = '', 
                                full_name = '', ), 
                            country_code = 'C201', 
                            address = openapi_client.models.simple_postal_address_(coarse_grained).Simple Postal Address (Coarse-Grained)(
                                line1 = '', 
                                line2 = '', 
                                city = '', 
                                state = '', 
                                country_code = 'C201', 
                                postal_code = '', ), ), 
                        shipping_info = openapi_client.models.shipping_information.Shipping Information(
                            name = '5''UOq1hlK5jZXw'V6.YZb0', 
                            method = '5''UOq1hlK5jZXw'V6.YZb0', 
                            secondary_shipping_address = openapi_client.models.simple_postal_address_(coarse_grained).Simple Postal Address (Coarse-Grained)(
                                line1 = '', 
                                line2 = '', 
                                city = '', 
                                state = '', 
                                country_code = 'C201', 
                                postal_code = '', ), ), 
                        cart_info = openapi_client.models.cart_information.Cart Information(
                            item_details = [
                                openapi_client.models.item_details.Item Details(
                                    item_code = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    item_name = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    item_description = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    item_options = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    item_quantity = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    item_unit_price = , 
                                    item_amount = , 
                                    adjustment_amount = , 
                                    gift_wrap_amount = , 
                                    tax_percentage = '-.2888001528021798096225500850', 
                                    tax_amounts = [
                                        openapi_client.models.tax_amount.Tax Amount(
                                            tax_amount = , )
                                        ], 
                                    basic_shipping_amount = , 
                                    extra_shipping_amount = , 
                                    handling_amount = , 
                                    total_item_amount = , 
                                    invoice_number = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    checkout_options = [
                                        openapi_client.models.checkout_option.Checkout Option(
                                            checkout_option_name = '5''UOq1hlK5jZXw'V6.YZb0', 
                                            checkout_option_value = '5''UOq1hlK5jZXw'V6.YZb0', )
                                        ], )
                                ], 
                            tax_inclusive = True, 
                            paypal_invoice_id = '5''UOq1hlK5jZXw'V6.YZb0', ), 
                        store_info = openapi_client.models.store_information.Store Information(
                            store_id = 'Cu2LC4aWwWL9Y864DZtaGR0', 
                            terminal_id = 'Cu2LC4aWwWL9Y864DZtaGR0', ), 
                        auction_info = openapi_client.models.auction_information.Auction Information(
                            auction_site = '5''UOq1hlK5jZXw'V6.YZb0', 
                            auction_item_site = '5''UOq1hlK5jZXw'V6.YZb0', 
                            auction_buyer_id = '5''UOq1hlK5jZXw'V6.YZb0', 
                            auction_closing_date = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819', ), 
                        incentive_info = openapi_client.models.incentive_information.Incentive Information(
                            incentive_details = [
                                openapi_client.models.incentive_details.Incentive Details(
                                    incentive_type = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    incentive_code = '5''UOq1hlK5jZXw'V6.YZb0', 
                                    incentive_amount = , 
                                    incentive_program_code = '5''UOq1hlK5jZXw'V6.YZb0', )
                                ], ), )
                    ],
                account_number = 'Cu2LC4aWwWL9Y864DZtaGR0',
                start_date = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819',
                end_date = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819',
                last_refreshed_datetime = '0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z012345678910111213141516171819',
                page = 0,
                total_items = 0,
                total_pages = 0,
                links = [
                    openapi_client.models.link_description.Link Description(
                        href = '', 
                        rel = '', 
                        method = 'GET', )
                    ]
            )
        else:
            return SearchResponse(
        )
        """

    def testSearchResponse(self):
        """Test SearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
