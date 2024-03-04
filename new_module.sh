#!/bin/bash

# Creates a new module with all possible files.
# controller, services, models, schemas.

if [[ -z "$1" ]]
  then
    echo "Usage:"
    echo "new_module.sh NEW_MODULE_NAME"
    exit 1
fi

NEW_MODULE=$1
MODULE_PATH="app/api/v1/$NEW_MODULE"

mkdir $MODULE_PATH

# Create __init__.py
cat << EOF > $MODULE_PATH/__init__.py
"""$NEW_MODULE module."""


EOF

# Create controllers.py
cat << EOF > $MODULE_PATH/controllers.py
"""API Route handlers for $NEW_MODULE."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.$NEW_MODULE import services
from app.database import db

router = APIRouter()


@router.post("/stub")
def stub(session: Session = Depends(db)):
    """Write documentation here."""
    pass

EOF

# Create services.py
cat << EOF > $MODULE_PATH/services.py
"""Services for $NEW_MODULE."""

EOF

# Create models.py
cat << EOF > $MODULE_PATH/models.py
"""DB Models for $NEW_MODULE."""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from app.database import Base


class Stub(Base):
    """Some database model."""

    __tablename__ = ""

    id: int = Column(Integer, primary_key=True, autoincrement=True)

EOF

# Create schemas.py
cat << EOF > $MODULE_PATH/schemas.py
"""Schemas for $NEW_MODULE."""

from pydantic import BaseModel


class Stub(BaseModel):
    """Stub schema."""

    some_string: str

EOF
