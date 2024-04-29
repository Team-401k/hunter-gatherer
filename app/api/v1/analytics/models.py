from sqlalchemy import Column, Float, PrimaryKeyConstraint, String

from app.database import Base

"each row is a month, and each of the analytics is a column"


class Analytics(Base):
    __tablename__ = "analytics"

    month = Column(String, nullable=False, index=True, unique=False)
    year = Column(String, nullable=False, index=True, unique=False)
    month_sales = Column(Float)
    month_fees = Column(Float)
    month_profit = Column(Float)
    ytd_sales = Column(Float)
    ytd_fees = Column(Float)
    ytd_profit = Column(Float)

    __table_args__ = (
        # Unique constraint to prevent duplicate entries
        # for the same month and year
        PrimaryKeyConstraint("month", "year", name="pk_analytics"),
    )

    def __repr__(self):
        return f"<Analytics {self.month}/{self.year}>"
