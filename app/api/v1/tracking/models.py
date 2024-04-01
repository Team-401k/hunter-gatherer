"""DB Models for tracking."""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from app.database import Base


class Tracking(Base):
    """Some database model."""

    __tablename__ = "tracking"

    current_cursor = Column(Integer, primary_key=True)
