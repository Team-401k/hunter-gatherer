"""Services for product_analytics."""

PRODUCT_ANALYTICS_QUERY = """
WITH unnested_orders AS (
    SELECT
        unnest(skus) AS sku,
        date,
        amount,
        fee
    FROM orders
)
SELECT
    sku as sku,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,

    ROUND(net_sales::numeric, 2) AS net_sales,
    ROUND(SUM(net_sales) OVER (PARTITION BY year ORDER BY month)::numeric, 2) AS ytd_net_sales,
"""


ANALYTICS_QUERY = """
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
"""
