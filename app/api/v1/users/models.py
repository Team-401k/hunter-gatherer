from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Boolean
from app.database import Base, current_utc_time
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email=Column(String, nullable=False)
    status = Column(String)
    types = Column(String)
    address = Column(String)
    phone = Column(String)
    usps = Column(String)
    date_joined = Column(Date)
    date_renewed = Column(Date)
    emergency_contact = Column(String)
    emergency_phone = Column(String)
    is_member = Column(Boolean)
    date_expired = Column(Date)


    def __repr__(self):
        return f"<User {self.username}>"
    
class Order(Base):
    __tablename__ = 'orders'

    purchase_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey('users.id'))  # Assuming users table with id as primary key
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, default=current_utc_time)
    type = Column(String, nullable=False) # Enum?
    method = Column(String)  # Enum?
    fee = Column(Float, default=0.0)
    stripe_paypal_id = Column(String) 

    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.purchase_id}>"
    