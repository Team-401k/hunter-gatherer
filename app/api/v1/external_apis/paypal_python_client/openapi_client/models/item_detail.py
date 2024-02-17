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
from openapi_client.models.checkout_option import CheckoutOption
from openapi_client.models.item_detail_tax_amount import ItemDetailTaxAmount
from openapi_client.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class ItemDetail(BaseModel):
    """
    The item details.
    """ # noqa: E501
    item_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1000)]] = Field(default=None, description="An item code that identifies a merchant's goods or service.")
    item_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(default=None, description="The item name.")
    item_description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(default=None, description="The item description.")
    item_options: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4000)]] = Field(default=None, description="The item options. Describes option choices on the purchase of the item in some detail.")
    item_quantity: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4000)]] = Field(default=None, description="The number of purchased units of goods or a service.")
    item_unit_price: Optional[Money] = None
    item_amount: Optional[Money] = None
    discount_amount: Optional[Money] = None
    adjustment_amount: Optional[Money] = None
    gift_wrap_amount: Optional[Money] = None
    tax_percentage: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as `19.99`.")
    tax_amounts: Optional[Annotated[List[ItemDetailTaxAmount], Field(min_length=1, max_length=32767)]] = Field(default=None, description="An array of tax amounts levied by a government on the purchase of goods or services.")
    basic_shipping_amount: Optional[Money] = None
    extra_shipping_amount: Optional[Money] = None
    handling_amount: Optional[Money] = None
    insurance_amount: Optional[Money] = None
    total_item_amount: Optional[Money] = None
    invoice_number: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(default=None, description="The invoice number. An alphanumeric string that identifies a billing for a merchant.")
    checkout_options: Optional[Annotated[List[CheckoutOption], Field(min_length=1, max_length=32767)]] = Field(default=None, description="An array of checkout options. Each option has a name and value.")
    __properties: ClassVar[List[str]] = ["item_code", "item_name", "item_description", "item_options", "item_quantity", "item_unit_price", "item_amount", "discount_amount", "adjustment_amount", "gift_wrap_amount", "tax_percentage", "tax_amounts", "basic_shipping_amount", "extra_shipping_amount", "handling_amount", "insurance_amount", "total_item_amount", "invoice_number", "checkout_options"]

    @field_validator('item_code')
    def item_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('item_name')
    def item_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('item_description')
    def item_description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('item_options')
    def item_options_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('item_quantity')
    def item_quantity_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('tax_percentage')
    def tax_percentage_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$", value):
            raise ValueError(r"must validate the regular expression /^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$/")
        return value

    @field_validator('invoice_number')
    def invoice_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
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
        """Create an instance of ItemDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of item_unit_price
        if self.item_unit_price:
            _dict['item_unit_price'] = self.item_unit_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_amount
        if self.item_amount:
            _dict['item_amount'] = self.item_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_amount
        if self.discount_amount:
            _dict['discount_amount'] = self.discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of adjustment_amount
        if self.adjustment_amount:
            _dict['adjustment_amount'] = self.adjustment_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift_wrap_amount
        if self.gift_wrap_amount:
            _dict['gift_wrap_amount'] = self.gift_wrap_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tax_amounts (list)
        _items = []
        if self.tax_amounts:
            for _item in self.tax_amounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tax_amounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of basic_shipping_amount
        if self.basic_shipping_amount:
            _dict['basic_shipping_amount'] = self.basic_shipping_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra_shipping_amount
        if self.extra_shipping_amount:
            _dict['extra_shipping_amount'] = self.extra_shipping_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of handling_amount
        if self.handling_amount:
            _dict['handling_amount'] = self.handling_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of insurance_amount
        if self.insurance_amount:
            _dict['insurance_amount'] = self.insurance_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_item_amount
        if self.total_item_amount:
            _dict['total_item_amount'] = self.total_item_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in checkout_options (list)
        _items = []
        if self.checkout_options:
            for _item in self.checkout_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkout_options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "item_code": obj.get("item_code"),
            "item_name": obj.get("item_name"),
            "item_description": obj.get("item_description"),
            "item_options": obj.get("item_options"),
            "item_quantity": obj.get("item_quantity"),
            "item_unit_price": Money.from_dict(obj["item_unit_price"]) if obj.get("item_unit_price") is not None else None,
            "item_amount": Money.from_dict(obj["item_amount"]) if obj.get("item_amount") is not None else None,
            "discount_amount": Money.from_dict(obj["discount_amount"]) if obj.get("discount_amount") is not None else None,
            "adjustment_amount": Money.from_dict(obj["adjustment_amount"]) if obj.get("adjustment_amount") is not None else None,
            "gift_wrap_amount": Money.from_dict(obj["gift_wrap_amount"]) if obj.get("gift_wrap_amount") is not None else None,
            "tax_percentage": obj.get("tax_percentage"),
            "tax_amounts": [ItemDetailTaxAmount.from_dict(_item) for _item in obj["tax_amounts"]] if obj.get("tax_amounts") is not None else None,
            "basic_shipping_amount": Money.from_dict(obj["basic_shipping_amount"]) if obj.get("basic_shipping_amount") is not None else None,
            "extra_shipping_amount": Money.from_dict(obj["extra_shipping_amount"]) if obj.get("extra_shipping_amount") is not None else None,
            "handling_amount": Money.from_dict(obj["handling_amount"]) if obj.get("handling_amount") is not None else None,
            "insurance_amount": Money.from_dict(obj["insurance_amount"]) if obj.get("insurance_amount") is not None else None,
            "total_item_amount": Money.from_dict(obj["total_item_amount"]) if obj.get("total_item_amount") is not None else None,
            "invoice_number": obj.get("invoice_number"),
            "checkout_options": [CheckoutOption.from_dict(_item) for _item in obj["checkout_options"]] if obj.get("checkout_options") is not None else None
        })
        return _obj

