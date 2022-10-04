from fastapi import APIRouter
from src.endpoints import products, users

router = APIRouter()
router.include_router(products.router)
router.include_router(users.router)
