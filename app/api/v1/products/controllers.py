"""API Route handlers for products."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.products import services
from app.database import db
from app.api.v1.products.models import Product


router = APIRouter()

@router.post("/sqsp_product_ingestion")
def ingest_sqsp_products(session: Session = Depends(db)):
    sqsp_products = services.get_products()
    for item in sqsp_products:
        new_product = Product(
            sku = item.sku,
            description = item.descriptor
        )

        session.add(new_product)
        session.commit()
