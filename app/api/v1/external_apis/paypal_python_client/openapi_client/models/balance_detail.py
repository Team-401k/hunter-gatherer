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

from pydantic import BaseModel, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class BalanceDetail(BaseModel):
    """
    The Balance information.
    """ # noqa: E501
    currency: Annotated[str, Field(min_length=3, strict=True, max_length=3)] = Field(description="The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.")
    primary: Optional[StrictBool] = Field(default=None, description="Optional field representing if the currency is primary currency or not.")
    total_balance: Money
    available_balance: Optional[Money] = None
    withheld_balance: Optional[Money] = None
    __properties: ClassVar[List[str]] = ["currency", "primary", "total_balance", "available_balance", "withheld_balance"]

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
        """Create an instance of BalanceDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of total_balance
        if self.total_balance:
            _dict['total_balance'] = self.total_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_balance
        if self.available_balance:
            _dict['available_balance'] = self.available_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of withheld_balance
        if self.withheld_balance:
            _dict['withheld_balance'] = self.withheld_balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BalanceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "primary": obj.get("primary"),
            "total_balance": Money.from_dict(obj["total_balance"]) if obj.get("total_balance") is not None else None,
            "available_balance": Money.from_dict(obj["available_balance"]) if obj.get("available_balance") is not None else None,
            "withheld_balance": Money.from_dict(obj["withheld_balance"]) if obj.get("withheld_balance") is not None else None
        })
        return _obj


