from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Boolean
from app.database import Base, current_utc_time
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    email=Column(String, nullable=False, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    date_joined = Column(DateTime)
    date_renewed = Column(DateTime)
    is_member = Column(Boolean)
        

    def __repr__(self):
        return f"<User {self.username}>"
    

    