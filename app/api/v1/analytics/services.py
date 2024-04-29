"""Services for analytics."""

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.v1.analytics.models import Analytics

ANALYTICS_QUERY = """
SELECT
    year as year,
    month as month,
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
) AS monthly_totals
ORDER BY year, month;
"""


def get_analytics(session: Session):
    """Get analytics."""
    return session.execute(text(ANALYTICS_QUERY)).fetchall()


def get_and_ingest_analytics(session: Session):
    """Ingest analytics."""
    analytics_results = get_analytics(session)
    for analytics in analytics_results:
        # Insert analytics into table
        new_analytic = Analytics(
            month=analytics.month,
            year=analytics.year,
            month_sales=analytics.net_sales,
            month_fees=analytics.net_fees,
            month_profit=analytics.net_profit,
            ytd_sales=analytics.ytd_net_sales,
            ytd_fees=analytics.ytd_net_fees,
            ytd_profit=analytics.ytd_net_profit,
        )
        session.add(new_analytic)
        session.flush()
    session.commit()
