import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from app.database import db

# Configure logging
logging.basicConfig(filename='daily_update.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Database credentials and connection
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Set up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

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

if __name__ == "__main__":
    execute_sql_queries()

