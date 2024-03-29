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

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.auction_info import AuctionInfo
from openapi_client.models.cart_info import CartInfo
from openapi_client.models.incentive_info import IncentiveInfo
from openapi_client.models.payer_info import PayerInfo
from openapi_client.models.shipping_info import ShippingInfo
from openapi_client.models.store_info import StoreInfo
from openapi_client.models.transaction_info import TransactionInfo
from typing import Optional, Set
from typing_extensions import Self

class TransactionDetail(BaseModel):
    """
    The transaction details.
    """ # noqa: E501
    transaction_info: Optional[TransactionInfo] = None
    payer_info: Optional[PayerInfo] = None
    shipping_info: Optional[ShippingInfo] = None
    cart_info: Optional[CartInfo] = None
    store_info: Optional[StoreInfo] = None
    auction_info: Optional[AuctionInfo] = None
    incentive_info: Optional[IncentiveInfo] = None
    __properties: ClassVar[List[str]] = ["transaction_info", "payer_info", "shipping_info", "cart_info", "store_info", "auction_info", "incentive_info"]

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
        """Create an instance of TransactionDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction_info
        if self.transaction_info:
            _dict['transaction_info'] = self.transaction_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer_info
        if self.payer_info:
            _dict['payer_info'] = self.payer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_info
        if self.shipping_info:
            _dict['shipping_info'] = self.shipping_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cart_info
        if self.cart_info:
            _dict['cart_info'] = self.cart_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of store_info
        if self.store_info:
            _dict['store_info'] = self.store_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auction_info
        if self.auction_info:
            _dict['auction_info'] = self.auction_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of incentive_info
        if self.incentive_info:
            _dict['incentive_info'] = self.incentive_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transaction_info": TransactionInfo.from_dict(obj["transaction_info"]) if obj.get("transaction_info") is not None else None,
            "payer_info": PayerInfo.from_dict(obj["payer_info"]) if obj.get("payer_info") is not None else None,
            "shipping_info": ShippingInfo.from_dict(obj["shipping_info"]) if obj.get("shipping_info") is not None else None,
            "cart_info": CartInfo.from_dict(obj["cart_info"]) if obj.get("cart_info") is not None else None,
            "store_info": StoreInfo.from_dict(obj["store_info"]) if obj.get("store_info") is not None else None,
            "auction_info": AuctionInfo.from_dict(obj["auction_info"]) if obj.get("auction_info") is not None else None,
            "incentive_info": IncentiveInfo.from_dict(obj["incentive_info"]) if obj.get("incentive_info") is not None else None
        })
        return _obj


