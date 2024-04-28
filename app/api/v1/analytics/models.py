from sqlalchemy import Column, String, Numeric

from app.database import Base

"each row is a month, and each of the analytics is a column"
class Analytics(Base):
    __tablename__ = "analytics"

    pk = Column(String, nullable=False, primary_key=True, index=True, unique=True)
    month = Column(String, nullable=False, index=True, unique=False)
    year = Column(String, nullable=False, index=True, unique=False)
    month_sales = Column(Numeric(12, 2), default=0)
    month_fees = Column(Numeric(12, 2), default=0)
    month_profit = Column(Numeric(12, 2), default=0)
    ytd_sales = Column(Numeric(12, 2), default=0)
    ytd_fees = Column(Numeric(12, 2), default=0)
    ytd_profit = Column(Numeric(12, 2), default=0)

    def __repr__(self):
        return f"<Analytics {self.pk}>"
