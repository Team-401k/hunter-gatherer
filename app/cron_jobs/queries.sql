-- Net Sales Per Month
SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(amount)::numeric, 2) AS net_sales
FROM orders
GROUP BY year, month;

-- Net Fees Per Month
SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(fee)::numeric, 2) AS net_fees
FROM orders
GROUP BY year, month;

-- Net Profit Per Month
SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(SUM(amount - fee)::numeric, 2) AS net_profit
FROM orders
GROUP BY year, month;

-- Year to Date Total Column by month
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

-- Per product breakdown of net-sales, fees, profit, and a year to date total
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


-- Per Product Breakdown grouped by sku and month
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

-- For treasurer report, query to sum up total sales, refunds, and calculate net sales after joining with the products table

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
