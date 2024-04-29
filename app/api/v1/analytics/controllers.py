"""API Route handlers for analytics."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.analytics import services
from app.database import db

router = APIRouter()


@router.post("/analytics")
def ingest_analytics(session: Session = Depends(db)):
    services.get_and_ingest_analytics(session)
