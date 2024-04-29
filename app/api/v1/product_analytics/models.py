from sqlalchemy import Column, Float, ForeignKey, PrimaryKeyConstraint, String

from app.database import Base


class ProductAnalytics(Base):
    __tablename__ = "product_analytics"

    sku = Column(String, ForeignKey("products.sku"), nullable=False)
    description = Column(String, nullable=False)
    month_sales = Column(Float)
    month_fees = Column(Float)
    month_profit = Column(Float)
    ytd_sales = Column(Float)
    ytd_fees = Column(Float)
    ytd_profit = Column(Float)
    month = Column(String, nullable=False, index=True, unique=False)
    year = Column(String, nullable=False, index=True, unique=False)

    __table_args__ = (
        # Unique constraint to prevent duplicate entries
        # for the same month and year
        PrimaryKeyConstraint("sku", "month", "year", name="pk_product_analytics"),
    )

    def __repr__(self):
        return f"<ProductAnalytics {self.sku}>"
