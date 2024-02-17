# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class TransactionInfo(BaseModel):
    """
    The transaction information.
    """ # noqa: E501
    paypal_account_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=24)]] = Field(default=None, description="The ID of the PayPal account of the counterparty.")
    transaction_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=24)]] = Field(default=None, description="The PayPal-generated transaction ID.")
    paypal_reference_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=24)]] = Field(default=None, description="The PayPal-generated base ID. PayPal exclusive. Cannot be altered. Defined as a related, pre-existing transaction or event.")
    paypal_reference_id_type: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="The PayPal reference ID type.")
    transaction_event_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=5)]] = Field(default=None, description="A five-digit transaction event code that classifies the transaction type based on money movement and debit or credit. For example, <code>T0001</code>. See [Transaction event codes](/docs/integration/direct/transaction-search/transaction-event-codes/).")
    transaction_initiation_date: Optional[Annotated[str, Field(min_length=20, strict=True, max_length=64)]] = Field(default=None, description="The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>")
    transaction_updated_date: Optional[Annotated[str, Field(min_length=20, strict=True, max_length=64)]] = Field(default=None, description="The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.<blockquote><strong>Note:</strong> The regular expression provides guidance but does not reject all invalid dates.</blockquote>")
    transaction_amount: Optional[Money] = None
    fee_amount: Optional[Money] = None
    discount_amount: Optional[Money] = None
    insurance_amount: Optional[Money] = None
    sales_tax_amount: Optional[Money] = None
    shipping_amount: Optional[Money] = None
    shipping_discount_amount: Optional[Money] = None
    shipping_tax_amount: Optional[Money] = None
    other_amount: Optional[Money] = None
    tip_amount: Optional[Money] = None
    transaction_status: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="A code that indicates the transaction status. Value is:<table><thead><tr><th>Status&nbsp;code</th><th>Description</th></tr></thead><tbody><tr><td><code>D</code></td><td>PayPal or merchant rules denied the transaction.</td></tr><tr><td><code>P</code></td><td>The transaction is pending. The transaction was created but waits for another payment process to complete, such as an ACH transaction, before the status changes to <code>S</code>.</td></tr><tr><td><code>S</code></td><td>The transaction successfully completed without a denial and after any pending statuses.</td></tr><tr><td><code>V</code></td><td>A successful transaction was fully reversed and funds were refunded to the original sender.</td></tr></tbody></table>")
    transaction_subject: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=256)]] = Field(default=None, description="The subject of payment. The payer passes this value to the payee. The payer controls this data through the interface through which he or she sends the data.")
    transaction_note: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4000)]] = Field(default=None, description="A special note that the payer passes to the payee. Might contain special customer requests, such as shipping instructions.")
    payment_tracking_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=127)]] = Field(default=None, description="The payment tracking ID, which is a unique ID that partners specify to either get information about a payment or request a refund.")
    bank_reference_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=127)]] = Field(default=None, description="The bank reference ID. The bank provides this value for an ACH transaction.")
    ending_balance: Optional[Money] = None
    available_balance: Optional[Money] = None
    invoice_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=127)]] = Field(default=None, description="The invoice ID that is sent by the merchant with the transaction.<blockquote><strong>Note:</strong> If an invoice ID was sent with the capture request, the value is reported. Otherwise, the invoice ID of the authorizing transaction is reported.</blockquote>")
    custom_field: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=127)]] = Field(default=None, description="The merchant-provided custom text.<blockquote><strong>Note:</strong> Usually, this field includes the unique ID for payments made with MassPay type transaction.</blockquote>")
    protection_eligibility: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2)]] = Field(default=None, description="Indicates whether the transaction is eligible for protection. Value is:<ul><li><code>01</code>. Eligible.</li><li><code>02</code>. Not eligible</li><li><code>03</code>. Partially eligible.</li></ul>")
    credit_term: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=25)]] = Field(default=None, description="The credit term. The time span covered by the installment payments as expressed in the term length plus the length time unit code.")
    credit_transactional_fee: Optional[Money] = None
    credit_promotional_fee: Optional[Money] = None
    annual_percentage_rate: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`.")
    payment_method_type: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=20)]] = Field(default=None, description="The payment method that was used for a transaction. Value is <code>PUI</code>, <code>installment</code>, or <code>mEFT</code>.<blockquote><strong>Note:</strong> Appears only for pay upon invoice (PUI), installment, and mEFT transactions. Merchants and partners in the EMEA region can use this attribute to note transactions that attract turn-over tax.</blockquote>")
    instrument_type: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=64)]] = Field(default=None, description="A high-level classification of the type of financial instrument that was used to fund a payment. The pattern is not provided because the value is defined by an external party. E.g. PAYPAL, CREDIT_CARD, DEBIT_CARD, APPLE_PAY, BANK , VENMO ,Pay Upon Invoice, Pay Later  or <a href=\"https://developer.paypal.com/docs/checkout/integration-features/alternative-payment-methods/\" title=\"Link to available APM list\">Alternative Payment Methods (APM)</a>.")
    instrument_sub_type: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=64)]] = Field(default=None, description="A finer-grained classification of the financial instrument that was used to fund a payment. For example, `Visa card` or a `Mastercard` for a credit card, BANKCARD ,DISCOVER etc. The pattern is not provided because the value is defined by an external party.")
    __properties: ClassVar[List[str]] = ["paypal_account_id", "transaction_id", "paypal_reference_id", "paypal_reference_id_type", "transaction_event_code", "transaction_initiation_date", "transaction_updated_date", "transaction_amount", "fee_amount", "discount_amount", "insurance_amount", "sales_tax_amount", "shipping_amount", "shipping_discount_amount", "shipping_tax_amount", "other_amount", "tip_amount", "transaction_status", "transaction_subject", "transaction_note", "payment_tracking_id", "bank_reference_id", "ending_balance", "available_balance", "invoice_id", "custom_field", "protection_eligibility", "credit_term", "credit_transactional_fee", "credit_promotional_fee", "annual_percentage_rate", "payment_method_type", "instrument_type", "instrument_sub_type"]

    @field_validator('paypal_account_id')
    def paypal_account_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('transaction_id')
    def transaction_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('paypal_reference_id')
    def paypal_reference_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('paypal_reference_id_type')
    def paypal_reference_id_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('paypal_reference_id_type')
    def paypal_reference_id_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ODR', 'TXN', 'SUB', 'PAP']):
            raise ValueError("must be one of enum values ('ODR', 'TXN', 'SUB', 'PAP')")
        return value

    @field_validator('transaction_event_code')
    def transaction_event_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('transaction_initiation_date')
    def transaction_initiation_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$/")
        return value

    @field_validator('transaction_updated_date')
    def transaction_updated_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$/")
        return value

    @field_validator('transaction_status')
    def transaction_status_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('transaction_subject')
    def transaction_subject_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('transaction_note')
    def transaction_note_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('payment_tracking_id')
    def payment_tracking_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('bank_reference_id')
    def bank_reference_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('invoice_id')
    def invoice_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('custom_field')
    def custom_field_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('protection_eligibility')
    def protection_eligibility_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('credit_term')
    def credit_term_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9.]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9.]*$/")
        return value

    @field_validator('annual_percentage_rate')
    def annual_percentage_rate_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$", value):
            raise ValueError(r"must validate the regular expression /^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$/")
        return value

    @field_validator('payment_method_type')
    def payment_method_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-]*$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "transaction_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction_amount
        if self.transaction_amount:
            _dict['transaction_amount'] = self.transaction_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee_amount
        if self.fee_amount:
            _dict['fee_amount'] = self.fee_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_amount
        if self.discount_amount:
            _dict['discount_amount'] = self.discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of insurance_amount
        if self.insurance_amount:
            _dict['insurance_amount'] = self.insurance_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_tax_amount
        if self.sales_tax_amount:
            _dict['sales_tax_amount'] = self.sales_tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_amount
        if self.shipping_amount:
            _dict['shipping_amount'] = self.shipping_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_discount_amount
        if self.shipping_discount_amount:
            _dict['shipping_discount_amount'] = self.shipping_discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_tax_amount
        if self.shipping_tax_amount:
            _dict['shipping_tax_amount'] = self.shipping_tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of other_amount
        if self.other_amount:
            _dict['other_amount'] = self.other_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tip_amount
        if self.tip_amount:
            _dict['tip_amount'] = self.tip_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ending_balance
        if self.ending_balance:
            _dict['ending_balance'] = self.ending_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_balance
        if self.available_balance:
            _dict['available_balance'] = self.available_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_transactional_fee
        if self.credit_transactional_fee:
            _dict['credit_transactional_fee'] = self.credit_transactional_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_promotional_fee
        if self.credit_promotional_fee:
            _dict['credit_promotional_fee'] = self.credit_promotional_fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paypal_account_id": obj.get("paypal_account_id"),
            "transaction_id": obj.get("transaction_id"),
            "paypal_reference_id": obj.get("paypal_reference_id"),
            "paypal_reference_id_type": obj.get("paypal_reference_id_type"),
            "transaction_event_code": obj.get("transaction_event_code"),
            "transaction_initiation_date": obj.get("transaction_initiation_date"),
            "transaction_updated_date": obj.get("transaction_updated_date"),
            "transaction_amount": Money.from_dict(obj["transaction_amount"]) if obj.get("transaction_amount") is not None else None,
            "fee_amount": Money.from_dict(obj["fee_amount"]) if obj.get("fee_amount") is not None else None,
            "discount_amount": Money.from_dict(obj["discount_amount"]) if obj.get("discount_amount") is not None else None,
            "insurance_amount": Money.from_dict(obj["insurance_amount"]) if obj.get("insurance_amount") is not None else None,
            "sales_tax_amount": Money.from_dict(obj["sales_tax_amount"]) if obj.get("sales_tax_amount") is not None else None,
            "shipping_amount": Money.from_dict(obj["shipping_amount"]) if obj.get("shipping_amount") is not None else None,
            "shipping_discount_amount": Money.from_dict(obj["shipping_discount_amount"]) if obj.get("shipping_discount_amount") is not None else None,
            "shipping_tax_amount": Money.from_dict(obj["shipping_tax_amount"]) if obj.get("shipping_tax_amount") is not None else None,
            "other_amount": Money.from_dict(obj["other_amount"]) if obj.get("other_amount") is not None else None,
            "tip_amount": Money.from_dict(obj["tip_amount"]) if obj.get("tip_amount") is not None else None,
            "transaction_status": obj.get("transaction_status"),
            "transaction_subject": obj.get("transaction_subject"),
            "transaction_note": obj.get("transaction_note"),
            "payment_tracking_id": obj.get("payment_tracking_id"),
            "bank_reference_id": obj.get("bank_reference_id"),
            "ending_balance": Money.from_dict(obj["ending_balance"]) if obj.get("ending_balance") is not None else None,
            "available_balance": Money.from_dict(obj["available_balance"]) if obj.get("available_balance") is not None else None,
            "invoice_id": obj.get("invoice_id"),
            "custom_field": obj.get("custom_field"),
            "protection_eligibility": obj.get("protection_eligibility"),
            "credit_term": obj.get("credit_term"),
            "credit_transactional_fee": Money.from_dict(obj["credit_transactional_fee"]) if obj.get("credit_transactional_fee") is not None else None,
            "credit_promotional_fee": Money.from_dict(obj["credit_promotional_fee"]) if obj.get("credit_promotional_fee") is not None else None,
            "annual_percentage_rate": obj.get("annual_percentage_rate"),
            "payment_method_type": obj.get("payment_method_type"),
            "instrument_type": obj.get("instrument_type"),
            "instrument_sub_type": obj.get("instrument_sub_type")
        })
        return _obj


