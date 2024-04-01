"""Services for orders."""

import enum
from typing import List, Optional

from sqlalchemy.orm import Session

import app.api.v1.users.services as user_services
from app.api.v1.external_apis.schemas import (
    Document,
    OrdersResponse,
    Profile,
    SqspOrderDetailResponse,
    SqspTransactionsResponse,
)
from app.api.v1.orders.models import Order


class OrderService(str, enum.Enum):
    PAYPAL = "paypal"
    STRIPE = "stripe"
    SQSP = "sqsp"


def get_orders(start_date: str, end_date: str) -> OrdersResponse:
    # First get the parsed orders from paypal
    # if origin == OrderService.PAYPAL:
    #     return paypal_api.search_parse(start_date, end_date)
    # elif origin == OrderService.STRIPE:
    #     return (stripe_api.search_parse(start_date, end_date)).data
    # elif origin == OrderService.SQSP:
    return sqsp_api.search_parse_orders_list(start_date, end_date)


def get_order_detail(order_id: str) -> SqspOrderDetailResponse:
    return sqsp_api.search_parse_order_detail(order_id)


def get_transactions_from_api(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None,
) -> SqspTransactionsResponse:
    return sqsp_api.search_parse_transactions(start_date, end_date, cursor)


def get_profile(email: str):
    return sqsp_api.search_parse_profile(email)


def parse_customizations(customizations):
    first_name = ""
    last_name = ""
    name = ""
    phone = ""
    email = ""
    address_line = ""
    city = ""
    state = ""
    postal_code = ""
    emergency_contact = ""
    emergency_contact_phone = ""

    for customization in customizations:
        if customization.label == "First Name":
            first_name = customization.value if customization.value else ""
        elif customization.label == "Last Name":
            last_name = customization.value if customization.value else ""
        elif customization.label == "Name":
            name = customization.value if customization.value else ""
        elif customization.label == "Phone":
            phone = customization.value if customization.value else ""
        elif customization.label == "Email":
            email = customization.value if customization.value else ""
        elif customization.label == "Address":
            address_line = customization.value if customization.value else ""
        elif customization.label == "City":
            city = customization.value if customization.value else ""
        elif customization.label == "State":
            state = customization.value if customization.value else ""
        elif customization.label == "Postal Code":
            postal_code = customization.value if customization.value else ""
        elif customization.label == "Emergency Contact Name":
            emergency_contact = customization.value if customization.value else ""
        elif customization.label == "Emergency Contact Phone":
            emergency_contact_phone = customization.value if customization.value else ""

    if first_name and not name:
        name = first_name + " " + last_name
    # elif name, nothing to do

    return (
        name.replace("\n", " "),
        phone,
        email.lower(),
        address_line,
        city,
        state,
        postal_code,
        emergency_contact,
        emergency_contact_phone,
    )


def parse_profile(profile: Profile):
    name = profile.firstName + " " + profile.lastName

    address = (
        profile.address.address1
        + " "
        + (profile.address.address2 or "")
        + ", "
        + profile.address.city
        + ", "
        + profile.address.state
        + " "
        + profile.address.postalCode
    )
    phone = profile.address.phone

    return name.replace("\n", " "), address, phone


def create_initial_order_object(transaction: Document):
    new_order = Order(
        sqsp_order_id=transaction.salesOrderId,
        user_emails=[],  # need to add user
        amount=transaction.total.value,
        date=transaction.createdOn,
        # add sku from line items later
        payment_platform=transaction.payments[0].provider,
        fee=transaction.total.value - transaction.totalNetPayment.value,
        external_transaction_id=transaction.payments[0].externalTransactionId,
        sqsp_transaction_id=transaction.id,
    )

    return new_order


def create_donation_order_and_upsert_user(
    session: Session,
    new_order: Order,
    transaction: Document,
) -> Order:
    new_order.sku = "SQDONATION"
    email = transaction.customerEmail.lower()
    user = user_services.get_user_by_email(session, email)
    if not user:
        profile: List[Profile] = get_profile(
            email,
        ).profiles
        name = ""
        address = ""
        phone = ""
        if profile:
            name, address, phone = parse_profile(profile[0])
        else:
            print(transaction.customerEmail)
        user = user_services.create_user(
            session,
            email,
            name,
            address,
            phone,
        )
    new_order.user_emails.append(user.email)

    return new_order


def create_product_order_and_upsert_users(
    session: Session,
    new_order: Order,
    transaction: Document,
    order_detail: SqspOrderDetailResponse,
) -> Order:
    for line_item in order_detail.lineItems:
        (
            name,
            phone,
            email,
            address_line,
            city,
            state,
            postal_code,
            emergency_contact,
            emergency_contact_phone,
        ) = parse_customizations(line_item.customizations)
        if not email:
            email = order_detail.customerEmail
        if not address_line:
            address_line = order_detail.billingAddress.address1
        if not city:
            city = order_detail.billingAddress.city
        if not state:
            state = order_detail.billingAddress.state
        if not postal_code:
            postal_code = order_detail.billingAddress.postalCode
        if not phone:
            phone = order_detail.billingAddress.phone

        address = address_line + ", " + city + ", " + state + " " + postal_code

        user = user_services.upsert_user(
            session,
            email,
            name,
            address,
            phone,
            emergency_contact,
            emergency_contact_phone,
        )

        # associate user with order
        new_order.user_emails.append(user.email)
        # add sku to order
        new_order.sku = line_item.sku

    return new_order
