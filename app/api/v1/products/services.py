"""Services for products."""

from typing import List

from sqlalchemy.orm import Session

from app.api.v1.external_apis.schemas import InventoryItem, SqspProductResponse
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI
from app.api.v1.products.models import Product

sqsp_api = SquareSpaceAPI()


def get_products_from_api() -> List[InventoryItem]:
    products = []
    has_next_page = True
    while has_next_page:
        products_response: SqspProductResponse = sqsp_api.search_parse_products()
        products.extend(products_response.inventory)
        has_next_page = products_response.pagination.hasNextPage

    return products


def get_existing_product_skus(session: Session) -> List[str]:
    skus = session.query(Product.sku.distinct().label("sku")).all()
    return set([sku.sku for sku in skus])
