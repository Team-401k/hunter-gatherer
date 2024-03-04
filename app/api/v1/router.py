from fastapi import APIRouter
from app.api.v1.squarespace.controllers import router as squarespace_router
from app.api.v1.users.controllers import router as users_router

router = APIRouter(prefix="/v1")

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(squarespace_router, prefix="/squarespace", tags=["squarespace"])