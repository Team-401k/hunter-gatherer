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
from typing import Optional, Set
from typing_extensions import Self

class ShippingInfo(BaseModel):
    """
    The shipping information.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=500)]] = Field(default=None, description="The recipient's name.")
    method: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=500)]] = Field(default=None, description="The shipping method that is associated with this order.")
    address: Optional[Address] = None
    secondary_shipping_address: Optional[Address] = None
    __properties: ClassVar[List[str]] = ["name", "method", "address", "secondary_shipping_address"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\'\-., \":;\!?]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_'\-., \":;\!?]*$/")
        return value

    @field_validator('method')
    def method_validate_regular_expression(cls, value):
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
        """Create an instance of ShippingInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_shipping_address
        if self.secondary_shipping_address:
            _dict['secondary_shipping_address'] = self.secondary_shipping_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShippingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "method": obj.get("method"),
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "secondary_shipping_address": Address.from_dict(obj["secondary_shipping_address"]) if obj.get("secondary_shipping_address") is not None else None
        })
        return _obj


