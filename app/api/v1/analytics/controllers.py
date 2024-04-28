"""API Route handlers for analytics."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import db

router = APIRouter()


@router.post("/stub")
def stub(session: Session = Depends(db)):
    """Write documentation here."""
