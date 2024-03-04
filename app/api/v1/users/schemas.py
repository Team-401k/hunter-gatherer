"""Schemas for users."""

from pydantic import BaseModel
from typing import Optional, Dict, Any


class Stub(BaseModel):
    """Stub schema."""

    some_string: str


class Address(BaseModel):
    city: str
    country: str
    line1: str
    line2: Optional[str]
    postal_code: str
    state: str


class BillingDetails(BaseModel):
    address: Address
    email: Optional[str]
    name: str
    phone: Optional[str]


class Checks(BaseModel):
    address_line1_check: str
    address_postal_code_check: str
    cvc_check: str


class Card(BaseModel):
    amount_authorized: int
    brand: str
    checks: Checks
    country: str
    exp_month: int
    exp_year: int
    fingerprint: str
    funding: str
    last4: str
    network: str


class PaymentMethodDetails(BaseModel):
    card: Card
    type: str


class Metadata(BaseModel):
    id: str
    idempotencyKey: str
    orderId: str
    websiteId: str


class Outcome(BaseModel):
    network_status: str
    reason: Optional[str]
    risk_level: str
    seller_message: str
    type: str


class PaymentResponse(BaseModel):
    amount: int
    amount_captured: int
    amount_refunded: int
    application: str
    application_fee: Optional[Any]
    application_fee_amount: Optional[Any]
    balance_transaction: str
    billing_details: BillingDetails
    calculated_statement_descriptor: str
    captured: bool
    created: int
    currency: str
    customer: Optional[Any]
    description: str
    destination: Optional[Any]
    dispute: Optional[Any]
    disputed: bool
    failure_balance_transaction: Optional[Any]
    failure_code: Optional[Any]
    failure_message: Optional[Any]
    fraud_details: Dict[str, Any]
    id: str
    invoice: Optional[Any]
    livemode: bool
    metadata: Metadata
    object: str
    on_behalf_of: Optional[Any]
    order: Optional[Any]
    outcome: Outcome
    paid: bool
    payment_intent: str
    payment_method: str
    payment_method_details: PaymentMethodDetails
    radar_options: Dict[str, Any]
    receipt_email: Optional[str]
    receipt_number: Optional[Any]
    receipt_url: str
    refunded: bool
    review: Optional[Any]
    shipping: Optional[Any]
    source: Optional[Any]
    source_transfer: Optional[Any]
    statement_descriptor: Optional[Any]
    statement_descriptor_suffix: Optional[Any]
    status: str
    transfer_data: Optional[Any]
    transfer_group: Optional[Any]
