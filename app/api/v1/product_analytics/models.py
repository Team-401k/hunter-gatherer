from sqlalchemy import Column, String, Numeric

from app.database import Base

"""entire table needs to regenerated (cleared and refilled) every month, so each row is a product and then each column is an analytic for that product. 
This also means that if you're looking at the table at any given time, every row in the table would have the same current month and year listed
The month and year columns are only even there just for clarity if someone is looking and is like wait are these last month's analytics or this month's"""
class ProductAnalytics(Base):
    __tablename__ = "product_analytics"

    sku = Column(String, primary_key=True, unique=True)
    description = Column(String, nullable=False)
    month_sales = Column(Numeric(12, 2), default=0)
    month_fees = Column(Numeric(12, 2), default=0)
    month_profit = Column(Numeric(12, 2), default=0)
    ytd_sales = Column(Numeric(12, 2), default=0)
    ytd_fees = Column(Numeric(12, 2), default=0)
    ytd_profit = Column(Numeric(12, 2), default=0)
    month = Column(String, nullable=False, index=True, unique=False)
    year = Column(String, nullable=False, index=True, unique=False)

    def __repr__(self):
        return f"<ProductAnalytics {self.pk}>"
