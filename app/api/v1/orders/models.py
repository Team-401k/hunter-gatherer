"""DB Models for orders."""

from sqlalchemy import DateTime, Float, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from app.database import Base, current_utc_time


class Order(Base):
    __tablename__ = 'orders'

    purchase_id = Column(String, primary_key=True, index=True)
    user_ids = Column(ARRAY(String), nullable=False)  # Assuming users table with id as primary key
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    sku = Column(String, ForeignKey('products.sku'), nullable=False)
    payment_method = Column(String)  # Enum?
    fee = Column(Float, default=0.0)
    foreign_transaction_id = Column(String)

    def __repr__(self):
        return f"<Order {self.purchase_id}>"
    
    # def __init__(
    #     self,
    #     id: str,
    #     orderNumber: str,
    #     total: str,
    #     createdOn: str,
    #     modifiedOn: str,
    #     customerEmail: str,
    #     billingAddress: str,
    # ):
    #     self.id = id
    #     self.orderNumber = orderNumber
    #     self.total = total
    #     self.createdOn = createdOn
    #     self.modifiedOn = modifiedOn
    #     self.customerEmail = customerEmail
    #     self.billingsAddress = billingAddress
