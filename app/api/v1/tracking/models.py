"""DB Models for tracking."""

from sqlalchemy import String
from sqlalchemy.sql.schema import Column

from app.database import Base


class Tracking(Base):
    """Some database model."""

    __tablename__ = "tracking"

    cursor = Column(String, primary_key=True)
