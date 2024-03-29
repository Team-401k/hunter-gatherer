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
from openapi_client.models.address import Address
from openapi_client.models.name import Name
from openapi_client.models.phone import Phone
from typing import Optional, Set
from typing_extensions import Self

class PayerInfo(BaseModel):
    """
    The payer information.
    """ # noqa: E501
    account_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=13)]] = Field(default=None, description="The PayPal` customer account ID.")
    email_address: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=254)]] = Field(default=None, description="The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and 255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>")
    phone_number: Optional[Phone] = None
    address_status: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="The address status of the payer. Value is either:<ul><li><code>Y</code>. Verified.</li><li><code>N</code>. Not verified.</li></ul>")
    payer_status: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="The status of the payer. Value is `Y` or `N`.")
    payer_name: Optional[Name] = None
    country_code: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]] = Field(default=None, description="The [two-character ISO 3166-1 code](/docs/integration/direct/rest/country-codes/) that identifies the country or region.<blockquote><strong>Note:</strong> The country code for Great Britain is <code>GB</code> and not <code>UK</code> as used in the top-level domain names for that country. Use the `C2` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.</blockquote>")
    address: Optional[Address] = None
    __properties: ClassVar[List[str]] = ["account_id", "email_address", "phone_number", "address_status", "payer_status", "payer_name", "country_code", "address"]

    @field_validator('account_id')
    def account_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
        return value

    @field_validator('email_address')
    def email_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.+@[^\"\-].+$", value):
            raise ValueError(r"must validate the regular expression /^.+@[^\"\-].+$/")
        return value

    @field_validator('address_status')
    def address_status_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[N|Y]$", value):
            raise ValueError(r"must validate the regular expression /^[N|Y]$/")
        return value

    @field_validator('payer_status')
    def payer_status_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[N|Y]$", value):
            raise ValueError(r"must validate the regular expression /^[N|Y]$/")
        return value

    @field_validator('country_code')
    def country_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([A-Z]{2}|C2)$", value):
            raise ValueError(r"must validate the regular expression /^([A-Z]{2}|C2)$/")
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
        """Create an instance of PayerInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of phone_number
        if self.phone_number:
            _dict['phone_number'] = self.phone_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer_name
        if self.payer_name:
            _dict['payer_name'] = self.payer_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PayerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_id": obj.get("account_id"),
            "email_address": obj.get("email_address"),
            "phone_number": Phone.from_dict(obj["phone_number"]) if obj.get("phone_number") is not None else None,
            "address_status": obj.get("address_status"),
            "payer_status": obj.get("payer_status"),
            "payer_name": Name.from_dict(obj["payer_name"]) if obj.get("payer_name") is not None else None,
            "country_code": obj.get("country_code"),
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None
        })
        return _obj


