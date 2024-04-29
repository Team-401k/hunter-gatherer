from sqlalchemy import Boolean, Column, DateTime, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    pk = Column(String, nullable=False, primary_key=True, index=True, unique=True)
    email = Column(String, nullable=False, index=True, unique=False)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    emergency_contact = Column(String)
    emergency_contact_phone = Column(String)
    date_renewed = Column(DateTime)
    is_member = Column(Boolean, default = False)
    first_joined = Column(DateTime)
    date_expired = Column(DateTime)
    profile_pic = Column(String)

    def __repr__(self):
        return f"<User {self.pk}>"
