"""API Route handlers for orders."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.orders.models import Order
from app.api.v1.orders import services
from app.database import db

router = APIRouter()


@router.post("/orders/ingestion")
def ingest_sqsp_orders(session: Session = Depends(db)):
    """Write documentation here."""

    order = Order(
       purchase_id=1,
        user_id=1,
        amount=1.0,
        date='2024-03-27 16:29:47.522126',
        type='type',
        method='method',
        fee=1.0,
        stripe_paypal_id='stripe_paypal_id',
    )

    # ping api
    # api returns list of pydantic objects
    for item in list:
        new_order = Order(**item.model_dump())
        session.add(new_order)
        session.commit()
