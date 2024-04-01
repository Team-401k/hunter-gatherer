"""DB Models for products."""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from app.database import Base


class Product(Base):
    """Some database model."""

    __tablename__ = "products"

    sku = Column(String, primary_key=True, unique=True)
    description = Column(String, nullable=False)
