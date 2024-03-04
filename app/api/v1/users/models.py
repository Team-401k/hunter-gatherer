

from sqlalchemy import Boolean, Column, Integer, String, Date
from app.database import Base, current_utc_time


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