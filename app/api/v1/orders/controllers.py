"""API Route handlers for orders."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from tqdm import tqdm
import logging
from tabulate import tabulate

from app.api.v1.external_apis.schemas import SqspTransactionsResponse
from app.api.v1.orders import services
from app.api.v1.orders.models import Order
from app.api.v1.tracking.models import Tracking
from app.database import db

router = APIRouter()

logging.basicConfig(filename='daily_update.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Global variable to store SQL commands
sql_commands = """
SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(amount)::numeric, 2) AS net_sales
FROM orders
GROUP BY year, month;

SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(fee)::numeric, 2) AS net_fees
FROM orders
GROUP BY year, month;

SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(amount - fee)::numeric, 2) AS net_profit
FROM orders
GROUP BY year, month;

SELECT
  year,
  month,
  ROUND(net_sales::numeric, 2) AS net_sales,
  ROUND(SUM(net_sales) OVER (PARTITION BY year ORDER BY month)::numeric, 2) AS ytd_net_sales,
  ROUND(net_fees::numeric, 2) AS net_fees,
  ROUND(SUM(net_fees) OVER (PARTITION BY year ORDER BY month)::numeric, 2) AS ytd_net_fees,
  ROUND(net_profit::numeric, 2) AS net_profit,
  ROUND(SUM(net_profit) OVER (PARTITION BY year ORDER BY month)::numeric, 2) AS ytd_net_profit
FROM (
  SELECT
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    SUM(amount) AS net_sales,
    SUM(fee) AS net_fees,
    SUM(amount - fee) AS net_profit
  FROM orders
  GROUP BY year, month
) AS monthly_totals;

WITH yearly_sales AS (
  SELECT
    p.description,
    EXTRACT(YEAR FROM o.date) AS year,
    SUM(o.amount) AS total_sales,
    SUM(o.fee) AS total_fees,
    SUM(o.amount - o.fee) AS total_profit
  FROM
    orders o,
    LATERAL UNNEST(o.skus) AS order_sku
    JOIN products p ON p.sku = order_sku
  GROUP BY
    p.description,
    year
)
SELECT
  description,
  year,
  ROUND(SUM(total_sales)::numeric, 2) AS net_sales_year,
  ROUND(SUM(total_fees)::numeric, 2) AS net_fees_year,
  ROUND(SUM(total_profit)::numeric, 2) AS net_profit_year
FROM yearly_sales
GROUP BY
  description,
  year
ORDER BY
  description,
  year;

SELECT
  sku,
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(amount)::numeric, 2) AS net_sales,
  ROUND(SUM(fee)::numeric, 2) AS net_fees,
  ROUND(SUM(amount - fee)::numeric, 2) AS net_profit
FROM (
  SELECT
    unnest(skus) AS sku,
    date,
    amount,
    fee
  FROM orders
) AS unnested_orders
GROUP BY sku, year, month;

SELECT
  EXTRACT(YEAR FROM o.date)::INTEGER AS year,
  EXTRACT(MONTH FROM o.date)::INTEGER AS month,
  ROUND(SUM(CASE WHEN p.description NOT LIKE 'Refund%' THEN o.amount ELSE 0 END)::numeric, 2) AS total_sales,
  ROUND(SUM(CASE WHEN p.description LIKE 'Refund%' THEN o.amount ELSE 0 END)::numeric, 2) AS total_refunds,
  ROUND((SUM(CASE WHEN p.description NOT LIKE 'Refund%' THEN o.amount ELSE 0 END) -
         SUM(CASE WHEN p.description LIKE 'Refund%' THEN o.amount ELSE 0 END))::numeric, 2) AS net_sales
FROM orders o
JOIN products p ON p.sku = ANY(o.skus)
GROUP BY year, month;
"""

@router.post("/execute_sql_queries")
def execute_sql_queries():
    # Start a database session
    db_session = next(db())
    result = db_session.execute(text(sql_commands)).fetchall()

    # Check if the result is empty
    if not result:
        print("No results found.")
        logging.info("No results found.")
        return

    # Format the decimal values in the result
    formatted_result = [
    ("Year", "Month", "Total Sales", "Total Refunds", "Net Sales"),  # Table headers
    ] + [
    (year, month, f'{total_sales:.2f}', f'{total_refunds:.2f}', f'{net_sales:.2f}')
    for year, month, total_sales, total_refunds, net_sales in result
    ]

    # Print the formatted result
    print("Query result:")
    table = tabulate(formatted_result, headers="firstrow", tablefmt="grid")
    print(table)

    logging.info("Query executed successfully.")
    logging.info(f"Query result:\n{table}")


@router.post("/sqsp_initial_ingestion")
def ingest_sqsp_initial_orders(session: Session = Depends(db)):
    has_next_page = True
    cursor = None
    tracking = session.query(Tracking).first()
    if tracking:
        cursor = tracking.cursor if tracking.cursor != "INITIAL" else None
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
    sqsp_transactions: SqspTransactionsResponse = services.get_transactions_from_api(
        # "2024-02-16T00:00:00Z",
        # "2024-03-10T23:59:59Z",
    )

    for transaction in tqdm(sqsp_transactions.documents):
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
