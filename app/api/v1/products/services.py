"""Services for products."""
from typing import List

from app.api.v1.external_apis.schemas import SqspProductResponse, InventoryItem
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI

sqsp_api = SquareSpaceAPI()


def get_products() -> List[InventoryItem]:
    products = []
    has_next_page = True
    while has_next_page:
        products_response: SqspProductResponse = sqsp_api.search_parse_products()
        products.extend(products_response.inventory)
        has_next_page = products_response.pagination.hasNextPage

    print(products)
    return products
