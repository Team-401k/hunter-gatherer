"""API Route handlers for orders."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_utilities import repeat_every
from sqlalchemy.orm import Session

from app.api.v1.analytics.controllers import ingest_analytics
from app.api.v1.external_apis.schemas import SqspTransactionsResponse
from app.api.v1.orders import services
from app.api.v1.orders.models import Order
from app.api.v1.products.controllers import ingest_sqsp_products
from app.api.v1.tracking.models import Tracking
from app.database import db

router = APIRouter()

# @router.on_event('startup')
# @repeat_every(seconds=10)
# def test():
#     print("running")


@router.on_event("startup")
@repeat_every(seconds=3600)
def call_ingestion():
    session = next(db())
    print("ingesting products")
    ingest_sqsp_products(session)
    print("ingesting orders")
    ingest_sqsp_orders(session)
    print("ingesting analytics")
    ingest_analytics(session)
    # print("ingersting ")
    print("ingestion complete")


@router.post("/")
def print_test():
    print("hello world")


@router.post("/sqsp_initial_ingestion")
def ingest_sqsp_initial_orders(session: Session = Depends(db)):
    has_next_page = True
    cursor = None
    print("ingesting initial orders")
    tracking = session.query(Tracking).first()
    if tracking:
        cursor = tracking.cursor if tracking.cursor != "INITIAL" else None
    while has_next_page:
        sqsp_transactions: SqspTransactionsResponse = (
            services.get_transactions_from_api(cursor=cursor)
        )
        print("ingesting initial orders loop")
        for transaction in sqsp_transactions.documents:
            existing_transaction = (
                session.query(Order)
                .filter(Order.sqsp_transaction_id == transaction.id)
                .first()
            )
            if existing_transaction:
                continue
            try:
                print("creating order")

                # create initial order
                new_order: Order = services.create_initial_order_object(transaction)
                # if no salesOrderId (sqsp_order_id) then it is a donation
                print("handling donation")
                if not transaction.salesOrderId:
                    # create donation and user object
                    new_order = services.create_donation_order_and_upsert_user(
                        session,
                        new_order,
                        transaction,
                    )
                    print("handling donation in if statement")
                else:
                    print("handling order and user creation")
                    # create an order + users from order details
                    order_detail = services.get_order_detail(transaction.salesOrderId)
                    print("order detail retrieved")
                    new_order = services.create_product_order_and_upsert_users(
                        session,
                        new_order,
                        transaction,
                        order_detail,
                    )
                    print(" order made")
                print("adding to session")
                session.add(new_order)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error processing transaction: {transaction.id} - {e}")
                print(f"Transaction: {transaction.model_dump()}")
                print(f"current cursor: {cursor}")
                current_cursor = session.query(Tracking).first()
                if current_cursor:
                    current_cursor.cursor = cursor if cursor else "INITIAL"
                    session.commit()
                else:
                    new_cursor = Tracking(cursor=cursor if cursor else "INITIAL")
                    session.add(new_cursor)
                    session.commit()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error processing transaction: {transaction.id}: {e}",
                )

        has_next_page = sqsp_transactions.pagination.hasNextPage
        cursor = sqsp_transactions.pagination.nextPageCursor


@router.post("/sqsp_daily_ingestion")
def ingest_sqsp_orders(session: Session = Depends(db)):
    has_next_page = True
    cursor = None
    while has_next_page:
        sqsp_transactions: SqspTransactionsResponse = (
            services.get_transactions_from_api(cursor=cursor)
        )

        for transaction in sqsp_transactions.documents:
            existing_transaction = (
                session.query(Order)
                .filter(Order.sqsp_transaction_id == transaction.id)
                .first()
            )
            if existing_transaction:
                continue
            try:
                # create initial order
                new_order: Order = services.create_initial_order_object(transaction)
                # if no salesOrderId (sqsp_order_id) then it is a donation
                if not transaction.salesOrderId:
                    # create donation and user object
                    new_order = services.create_donation_order_and_upsert_user(
                        session,
                        new_order,
                        transaction,
                    )
                else:
                    # create an order + users from order details
                    order_detail = services.get_order_detail(transaction.salesOrderId)
                    new_order = services.create_product_order_and_upsert_users(
                        session,
                        new_order,
                        transaction,
                        order_detail,
                    )

                session.add(new_order)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error processing transaction: {transaction.id} - {e}")
                print(f"Transaction: {transaction.model_dump()}")
                print(f"current cursor: {cursor}")
                break
                # raise HTTPException(
                #     status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                #     detail=f"Error processing transaction: {transaction.id}: {e}",
                # )

        has_next_page = sqsp_transactions.pagination.hasNextPage
        cursor = sqsp_transactions.pagination.nextPageCursor


# @router.post("/sqsp_ingestion")
# def ingest_sqsp_orders(session: Session = Depends(db)):
#     """Write documentation here."""
#     sqsp_orders: OrdersResponse = services.get_orders(
#         services.OrderService.SQSP,
#         "2024-02-16T00:00:00Z",
#         "2024-03-10T23:59:59Z",
#     )
#     # ping api
#     # api returns list of pydantic objects
#     for item in sqsp_orders.result:
#         line_items_size = len(item.lineItems)
#         if line_items_size > 1:
#             new_order = Order(
#                 purchase_id=item.id,
#                 amount=item.grandTotal.value,
#                 date=item.createdOn,
#                 type="sqsp",
#                 method="method",
#                 fee=0.0,
#                 stripe_paypal_id=None,
#             )
#             # session.add(new_order)
#             # session.commit()
#             for i in range(line_items_size):
#                 if "forum" in item.lineItems[i].productName.lower():
#                     new_user = User(
#                         email=item.customerEmail,
#                         name=item.billingAddress.firstName
#                         + item.billingAddress.lastName,
#                         address=item.billingAddress.address1
#                         + item.billingAddress.address2
#                         + ", "
#                         + item.billingAddress.city
#                         + ", "
#                         + item.billingAddress.state
#                         + " "
#                         + item.billingAddress.postalCode,
#                         phone=item.billingAddress.phone,
#                     )
#                     session.add(new_user)
#                     session.commit()
#                 elif "membership" in item.lineItems[i].productName.lower():
#                     new_user = User(
#                         email=item.customerEmail,
#                         name=item.billingAddress.name,
#                         address=item.billingAddress.address1
#                         + item.billingAddress.address2
#                         + ", "
#                         + item.billingAddress.city
#                         + ", "
#                         + item.billingAddress.state
#                         + " "
#                         + item.billingAddress.postalCode,
#                     )
#                     session.add(new_user)
#                     session.commit()

#         else:
#             new_order = Order(
#                 purchase_id=item.id,
#                 amount=item.grandTotal.value,
#                 date=item.createdOn,
#                 type="sqsp",
#                 method="method",
#                 fee=0.0,
#                 stripe_paypal_id=None,
#             )
#             session.add(new_order)
#             session.commit()
#             if "forum" in item.lineItems[0].productName.lower():
#                 new_user = User(
#                     email=item.customerEmail,
#                     name=item.billingAddress.firstName + item.billingAddress.lastName,
#                     address=item.billingAddress.address1
#                     + item.billingAddress.address2
#                     + ", "
#                     + item.billingAddress.city
#                     + ", "
#                     + item.billingAddress.state
#                     + " "
#                     + item.billingAddress.postalCode,
#                 )
#                 session.add(new_user)
#                 session.commit()
#             elif "membership" in item.lineItems[0].productName.lower():
#                 new_user = User(
#                     email=item.customerEmail,
#                     name=item.billingAddress.name,
#                     address=item.billingAddress.address1
#                     + item.billingAddress.address2
#                     + ", "
#                     + item.billingAddress.city
#                     + ", "
#                     + item.billingAddress.state
#                     + " "
#                     + item.billingAddress.postalCode,
#                 )
#                 session.add(new_user)
#                 session.commit()

#         # break


# # @router.post("/stripe_ingestion")
# # def ingest_stripe_orders(session: Session = Depends(db)):
# #     stripe_orders = services.get_orders(services.OrderService.STRIPE, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
# #     for item in stripe_orders:
# #         new_order = Order(**item.model_dump())
# #         session.add(new_order)
# #         session.commit()


# # @router.post("/paypal_ingestion")
# # def ingest_pp_orders(session: Session = Depends(db)):
# #     pp_orders = services.get_orders(services.OrderService.PAYPAL, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
# #     for item in pp_orders:
# #         new_order = Order(**item.model_dump())
# #         session.add(new_order)
# #         session.commit()
