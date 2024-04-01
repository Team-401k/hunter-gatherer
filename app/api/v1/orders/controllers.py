"""API Route handlers for orders."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.external_apis.schemas import OrdersResponse, SqspTransactionsResponse
from app.api.v1.orders.models import Order
from app.api.v1.orders import services
from app.api.v1.users.models import User
from app.api.v1.users.services import get_user_by_email
from app.database import db
from app.api.v1.external_apis.pp_api import PayPalAPI
from app.api.v1.external_apis.stripe_api import StripeAPI
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI


router = APIRouter()

@router.post("/sqsp_ingestion")
def ingest_sqsp_orders(session: Session = Depends(db)):
    sqsp_transactions: SqspTransactionsResponse = services.get_transactions('2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
    for transaction in sqsp_transactions.documents:
        # create order
        new_order = Order(
            purchase_id=transaction.salesOrderId,
            user_ids=[], # need to add user
            amount=transaction.total.value,
            date = transaction.createdOn,
            # add sku from line items later
            payment_method=transaction.payments[0].provider,
            fee=transaction.total.value - transaction.totalNetPayment.value,
            external_transaction_id=transaction.payments[0].externalTransactionId,
        )

        # if transaction has salesOrderId then it is a product order
        # otherwise donation
        if not transaction.salesOrderId:
        # create donation
            pass
        else:
            # create an order + user (if needed) from order details
            order_detail = services.get_order_detail(transaction.salesOrderId)
            for line_item in order_detail.lineItems:
                if 'forum' in line_item.productName.lower():
                    first_name, last_name, phone, email = services.parse_forum_customizations(line_item.customizations)
    
                    name = first_name + " " + last_name
                    address = order_detail.billingAddress.address1 + " " + order_detail.billingAddress.address2 + ", " + order_detail.billingAddress.city + ", " + order_detail.billingAddress.state + " " + order_detail.billingAddress.postalCode

                    user = get_user_by_email(email)
                    if not user:
                        user = User(
                            email=email,
                            name=name,
                            address=address,
                            phone=phone,
                        )

                        session.add(user)
                        session.flush()
                        session.refresh(user)

                    new_order.user_ids.append(new_user.id)
                elif 'membership' in line_item.productName.lower():
                    address_line, city, state, postal_code, phone, name, email, emergency_contact, emergency_contact_phone = services.parse_membership_customizations(line_item.customizations)

                    address = address_line + ", " + city + ", " + state + " " + postal_code
                    # need to add check for if user exists or not
                    new_user = User(
                        email=email,
                        name=name,
                        address=address,
                        phone=phone,
                        emergency_contact=emergency_contact,
                        emergency_contact_phone=emergency_contact_phone,
                    )

                    session.add(new_user)
                    session.flush()                 
                    new_order.user_ids.append(new_user.id)



@router.post("/sqsp_ingestion")
def ingest_sqsp_orders(session: Session = Depends(db)):
    """Write documentation here."""
    sqsp_orders: OrdersResponse = services.get_orders(services.OrderService.SQSP, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
    # ping api
    # api returns list of pydantic objects
    for item in sqsp_orders.result:
        line_items_size = len(item.lineItems)
        if line_items_size > 1: 
            new_order = Order(
                purchase_id=item.id,
                amount=item.grandTotal.value,
                date=item.createdOn,
                type='sqsp',
                method='method',
                fee=0.0,
                stripe_paypal_id=None,
            )
            # session.add(new_order)
            # session.commit()  
            for i in range(line_items_size):
                if 'forum' in item.lineItems[i].productName.lower():
                    new_user = User(
                        email=item.customerEmail,
                        name=item.billingAddress.firstName + item.billingAddress.lastName,
                        address=item.billingAddress.address1 + item.billingAddress.address2 + ', ' + item.billingAddress.city + ', ' + item.billingAddress.state + ' ' + item.billingAddress.postalCode,
                        phone=item.billingAddress.phone,

                    )
                    session.add(new_user)
                    session.commit()
                elif 'membership' in item.lineItems[i].productName.lower():
                    new_user = User(
                        email=item.customerEmail,
                        name=item.billingAddress.name,
                        address=item.billingAddress.address1 + item.billingAddress.address2 + ', ' + item.billingAddress.city + ', ' + item.billingAddress.state + ' ' + item.billingAddress.postalCode,
                    )
                    session.add(new_user)
                    session.commit()


        else:
            new_order = Order(
                purchase_id=item.id,
                amount=item.grandTotal.value,
                date=item.createdOn,
                type='sqsp',
                method='method',
                fee=0.0,
                stripe_paypal_id=None,
            )
            session.add(new_order)
            session.commit()
            if 'forum' in item.lineItems[0].productName.lower():
                new_user = User(
                    email=item.customerEmail,
                    name=item.billingAddress.firstName + item.billingAddress.lastName,
                    address=item.billingAddress.address1 + item.billingAddress.address2 + ', ' + item.billingAddress.city + ', ' + item.billingAddress.state + ' ' + item.billingAddress.postalCode,
                )
                session.add(new_user)
                session.commit()
            elif 'membership' in item.lineItems[0].productName.lower():
                new_user = User(
                    email=item.customerEmail,
                    name=item.billingAddress.name,
                    address=item.billingAddress.address1 + item.billingAddress.address2 + ', ' + item.billingAddress.city + ', ' + item.billingAddress.state + ' ' + item.billingAddress.postalCode,
                )
                session.add(new_user)
                session.commit()

        


        
        # break


# @router.post("/stripe_ingestion")
# def ingest_stripe_orders(session: Session = Depends(db)):
#     stripe_orders = services.get_orders(services.OrderService.STRIPE, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
#     for item in stripe_orders:
#         new_order = Order(**item.model_dump())
#         session.add(new_order)
#         session.commit()


# @router.post("/paypal_ingestion")
# def ingest_pp_orders(session: Session = Depends(db)):
#     pp_orders = services.get_orders(services.OrderService.PAYPAL, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
#     for item in pp_orders:
#         new_order = Order(**item.model_dump())
#         session.add(new_order)
#         session.commit()


