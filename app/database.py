import datetime
from typing import Any, Generator, Type, TypeVar

from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, as_declarative, scoped_session, sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime

from app.config import settings

# DB CONNECTION ----------------------------------------------------------------
engine = create_engine(
    str(settings.DATABASE_URL),
    pool_timeout=10,
    connect_args={
        "connect_timeout": 10,
        "options": "-c statement_timeout=1800000",  # 30 minutes = 1800000 Milliseconds
    },
    pool_size=10,
    max_overflow=80,
    echo=settings.DATABASE_ECHO,
    pool_pre_ping=True,  # check connection before using
)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def db() -> Generator[Session, None, None]:
    """Dependency for FastAPI Routes.
    Generates a DB session to use in each request.

    Yields:
        Database session
    """
    session = scoped_session(session_factory)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


# ---------- BASE DB MODEL -----------------------------------------------------

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

meta = MetaData(naming_convention=convention)


def current_utc_time():
    return datetime.datetime.utcnow()


Self = TypeVar("Self", bound="Base")

# class for views
ViewBase = declarative_base()


@as_declarative(metadata=meta)
class Base:
    """
    Base for all models.

    It has some type definitions to
    enhance autocompletion.
    """

    __tablename__: str
    __table__: Table

    # Add created and updated timestamps to all tables/models
    created_at = Column(DateTime, default=current_utc_time)
    updated_at = Column(DateTime, default=current_utc_time, onupdate=current_utc_time)

    @classmethod
    def get(cls: Type[Self], session: Session, ident: Any) -> Self:
        """Get a model by its primary key."""
        return session.query(cls).get(ident)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
