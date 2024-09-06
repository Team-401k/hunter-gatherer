"""API Route handlers for analytics."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utilities import repeat_every

from app.api.v1.analytics import services
from app.database import db

router = APIRouter()

####  Do the following lines need to be uncommented??

# @router.on_event("startup")
# @repeat_every(seconds=3600)
# def call_analytics_ingestion():
#     session = next(db())
#     print("ingesting analytics")
#     ingest_analytics(session)
#     print("analytics ingestion complete")



@router.post("/analytics")
def ingest_analytics(session: Session = Depends(db)):
    services.get_and_ingest_analytics(session)
