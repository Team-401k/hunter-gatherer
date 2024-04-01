"""pydantic models"""

from pydantic import BaseModel, validator, Field
from typing import List, Optional
from datetime import datetime


####### Stripe ########

class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    line1: Optional[str] = None
    line2: Optional[str] = None
    postal_code: Optional[str] = None
    state: Optional[str] = None

class BillingDetails(BaseModel):
    address: Address
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None

class CardDetails(BaseModel):
    brand: Optional[str] = None
    checks: Optional[dict] = None
    country: Optional[str] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    funding: Optional[str] = None
    last4: Optional[str] = None

class PaymentMethodDetails(BaseModel):
    card: Optional[CardDetails] = None
    type: Optional[str] = None

class Metadata(BaseModel):
    id: Optional[str] = None
    idempotencyKey: Optional[str] = Field(None, alias="idempotency_key")
    orderId: Optional[str] = Field(None, alias="order_id")
    websiteId: Optional[str] = Field(None, alias="website_id")

class Charge(BaseModel): ###### main model ######
    id: str
    amount: int
    amount_captured: int
    amount_refunded: int
    application: Optional[str] = None
    application_fee: Optional[str] = None
    application_fee_amount: Optional[str] = None
    billing_details: BillingDetails
    captured: bool
    created: int
    currency: str
    description: Optional[str] = None
    metadata: Metadata
    payment_method_details: PaymentMethodDetails

class ChargesResponse(BaseModel):
    data: List[Charge]
    has_more: bool
    object: str
    url: str

####### End of Stripe #######

class Stub(BaseModel):
    """Stub schema."""

    some_string: str


######## Paypal #########
class TransactionAmount(BaseModel):
    currency_code: str
    value: str

class TransactionInfo(BaseModel): #### main model ####
    transaction_id: str
    transaction_event_code: str
    transaction_initiation_date: datetime
    transaction_updated_date: datetime
    transaction_amount: TransactionAmount
    transaction_status: str
    bank_reference_id: Optional[str] = None
    ending_balance: TransactionAmount
    available_balance: TransactionAmount
    protection_eligibility: str

    @validator('transaction_updated_date', 'transaction_initiation_date', pre=True)
    def parse_date(cls, value):
        return datetime.fromisoformat(value.replace('Z', '+00:00'))

###### End of Paypal ########
    

####### SquareSpace ########
class PriceInfo(BaseModel):
    value: str
    currency: str

class BillingAddress(BaseModel):
    firstName: str
    lastName: str
    address1: str
    address2: Optional[str]
    city: str
    state: str
    countryCode: str
    postalCode: str
    phone: Optional[str]

class LineItem(BaseModel):
    id: str
    variantId: Optional[str]
    sku: Optional[str]
    productId: str
    productName: str
    quantity: int
    unitPricePaid: PriceInfo
    imageUrl: Optional[str]
    lineItemType: Optional[str]

class Order(BaseModel): ##### main Model #####
    id: str
    orderNumber: str
    createdOn: datetime
    modifiedOn: datetime
    customerEmail: str
    billingAddress: BillingAddress
    lineItems: List[LineItem]
    grandTotal: PriceInfo

    @validator('createdOn', 'modifiedOn', pre=True)
    def parse_date(cls, value):
        return datetime.fromisoformat(value.replace('Z', '+00:00'))

class OrdersResponse(BaseModel):
    result: List[Order]
    pagination: dict

###### End of SquareSpace ######
    
##### Squarespace Transactions Schemas #####
class TotalSales(BaseModel):
    value: str
    currency: str


class TotalNetSales(BaseModel):
    value: str
    currency: str


class TotalNetShipping(BaseModel):
    value: str
    currency: str


class TotalTaxes(BaseModel):
    value: str
    currency: str


class Total(BaseModel):
    value: str
    currency: str


class TotalNetPayment(BaseModel):
    value: str
    currency: str


class Amount(BaseModel):
    value: str
    currency: str


class RefundedAmount(BaseModel):
    value: str
    currency: str


class NetAmount(BaseModel):
    value: str
    currency: str


class ProcessingFeeAmount(BaseModel):
    value: str
    currency: str


class AmountGatewayCurrency(BaseModel):
    value: str
    currency: str


class ProcessingFeeRefundedAmount(BaseModel):
    value: str
    currency: str


class RefundedAmountGatewayCurrency(BaseModel):
    value: str
    currency: str


class ProcessingFeeNetAmount(BaseModel):
    value: str
    currency: str


class NetAmountGatewayCurrency(BaseModel):
    value: str
    currency: str


class ProcessingFee(BaseModel):
    id: str
    amount: ProcessingFeeAmount
    amountGatewayCurrency: AmountGatewayCurrency
    exchangeRate: int
    refundedAmount: ProcessingFeeRefundedAmount
    refundedAmountGatewayCurrency: RefundedAmountGatewayCurrency
    netAmount: ProcessingFeeNetAmount
    netAmountGatewayCurrency: NetAmountGatewayCurrency
    feeRefunds: List


class Payment(BaseModel):
    id: str
    amount: Amount
    refundedAmount: RefundedAmount
    netAmount: NetAmount
    creditCardType: Optional[str]
    provider: str
    refunds: List
    processingFees: List[ProcessingFee]
    giftCardId: str
    paidOn: str
    externalTransactionId: str
    externalTransactionProperties: List
    externalCustomerId: str


class DiscountAmount(BaseModel):
    value: str
    currency: str


class TotalSales1(BaseModel):
    value: str
    currency: str


class TotalNetSales1(BaseModel):
    value: str
    currency: str


class Total1(BaseModel):
    value: str
    currency: str


class SalesLineItem(BaseModel):
    id: str
    discountAmount: DiscountAmount
    totalSales: TotalSales1
    totalNetSales: TotalNetSales1
    total: Total1
    taxes: List


class Document(BaseModel):
    id: str
    createdOn: str
    modifiedOn: str
    customerEmail: str
    salesOrderId: Optional[str]
    voided: bool
    totalSales: TotalSales
    totalNetSales: TotalNetSales
    totalNetShipping: TotalNetShipping
    totalTaxes: TotalTaxes
    total: Total
    totalNetPayment: TotalNetPayment
    payments: List[Payment]
    salesLineItems: List[SalesLineItem]
    discounts: List
    shippingLineItems: List
    paymentGatewayError: str


class Pagination(BaseModel):
    nextPageUrl: Optional[str]
    nextPageCursor: Optional[str]
    hasNextPage: bool


class SqspTransactionsResponse(BaseModel):
    documents: List[Document]
    pagination: Pagination

##### End of Squarespace Transactions Schemas #####

##### Squarespace Products Schemas #####
class InventoryItem(BaseModel):
    variantId: str
    sku: str
    descriptor: str
    quantity: int
    isUnlimited: bool


class Pagination(BaseModel):
    nextPageUrl: Optional[str] = None
    nextPageCursor: Optional[str] = None
    hasNextPage: bool


class SqspProductResponse(BaseModel):
    inventory: List[InventoryItem]
    pagination: Pagination

##### End of Squarespace Products Schemas #####