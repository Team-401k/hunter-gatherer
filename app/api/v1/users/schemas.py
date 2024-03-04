"""Schemas for users."""

from pydantic import BaseModel
from typing import Optional


class Stub(BaseModel):
    """Stub schema."""

    some_string: str


class TransactionAmount(BaseModel):
    currency_code: str
    value: str

class TransactionInfo(BaseModel):
    transaction_id: str
    transaction_event_code: str
    transaction_initiation_date: str
    transaction_updated_date: str
    transaction_amount: TransactionAmount
    transaction_status: str
    bank_reference_id: Optional[str] = None
    ending_balance: TransactionAmount
    available_balance: TransactionAmount
    protection_eligibility: str
