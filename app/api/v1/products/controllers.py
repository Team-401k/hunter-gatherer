"""API Route handlers for products."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.products import services
from app.database import db

router = APIRouter()


@router.post("/stub")
def stub(session: Session = Depends(db)):
    """Write documentation here."""
    pass

