"""Schemas for orders."""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class Address(BaseModel):
    firstName: str
    lastName: str
    address1: str
    address2: str
    city: str
    state: str
    countryCode: str
    postalCode: str


class GrandTotal(BaseModel):
    currency: str
    value: float


class OrderSchema(BaseModel):
    """Stub schema."""

    id: str
    orderNumber: str
    createdOn: datetime
    modifiedOn: datetime
    customerEmail: str
    billingAddress: Address
    grandTotal: GrandTotal


class OrderWrapper(BaseModel):
    result: List[OrderSchema]
