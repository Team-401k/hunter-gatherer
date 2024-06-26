"""API Route handlers for products."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.products import services
from app.api.v1.products.models import Product
from app.database import db

router = APIRouter()


@router.post("/sqsp_product_ingestion")
def ingest_sqsp_products(session: Session = Depends(db)):
    sqsp_products = services.get_products_from_api()
    existing_skus = services.get_existing_product_skus(session)
    for item in sqsp_products:
        if item.sku in existing_skus:
            continue
        new_product = Product(
            sku=item.sku,
            description=item.descriptor,
        )

        # print(f"Adding product {new_product.sku} to the database")
        session.add(new_product)
        session.commit()
