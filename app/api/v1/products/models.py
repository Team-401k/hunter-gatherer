"""DB Models for products."""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from app.database import Base


class Product(Base):
    """Some database model."""

    __tablename__ = "products"

    sku = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


