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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Name(BaseModel):
    """
    The name of the party.
    """ # noqa: E501
    prefix: Optional[Annotated[str, Field(strict=True, max_length=140)]] = Field(default=None, description="The prefix, or title, to the party's name.")
    given_name: Optional[Annotated[str, Field(strict=True, max_length=140)]] = Field(default=None, description="When the party is a person, the party's given, or first, name.")
    surname: Optional[Annotated[str, Field(strict=True, max_length=140)]] = Field(default=None, description="When the party is a person, the party's surname or family name. Also known as the last name. Required when the party is a person. Use also to store multiple surnames including the matronymic, or mother's, surname.")
    middle_name: Optional[Annotated[str, Field(strict=True, max_length=140)]] = Field(default=None, description="When the party is a person, the party's middle name. Use also to store multiple middle names including the patronymic, or father's, middle name.")
    suffix: Optional[Annotated[str, Field(strict=True, max_length=140)]] = Field(default=None, description="The suffix for the party's name.")
    alternate_full_name: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(default=None, description="DEPRECATED. The party's alternate name. Can be a business name, nickname, or any other name that cannot be split into first, last name. Required when the party is a business.")
    full_name: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(default=None, description="When the party is a person, the party's full name.")
    __properties: ClassVar[List[str]] = ["prefix", "given_name", "surname", "middle_name", "suffix", "alternate_full_name", "full_name"]

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
        """Create an instance of Name from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Name from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prefix": obj.get("prefix"),
            "given_name": obj.get("given_name"),
            "surname": obj.get("surname"),
            "middle_name": obj.get("middle_name"),
            "suffix": obj.get("suffix"),
            "alternate_full_name": obj.get("alternate_full_name"),
            "full_name": obj.get("full_name")
        })
        return _obj


