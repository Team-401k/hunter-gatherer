from fastapi import APIRouter
from app.api.v1.squarespace.controllers import router as squarespace_router
from app.api.v1.users.controllers import router as users_router
from app.api.v1.orders.controllers import router as orders_router
from app.api.v1.products.controllers import router as products_router

router = APIRouter(prefix="/v1")

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(orders_router, prefix="/orders", tags=["orders"])
router.include_router(squarespace_router, prefix="/squarespace", tags=["squarespace"])
router.include_router(products_router, prefix="/products", tags=["products"])