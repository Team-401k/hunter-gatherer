from fastapi import APIRouter

from app.api.v1.analytics.controllers import router as analytics_router
from app.api.v1.orders.controllers import router as orders_router
from app.api.v1.products.controllers import router as products_router
from app.api.v1.users.controllers import router as users_router

router = APIRouter(prefix="/v1")

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(orders_router, prefix="/orders", tags=["orders"])
router.include_router(products_router, prefix="/products", tags=["products"])
router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
