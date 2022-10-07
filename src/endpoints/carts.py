from fastapi import APIRouter, Request
from typing import List
from src.models.carts import Cart


router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/",response_description="Get all carts", response_model=List[Cart])
def return_cart(request: Request):
    
    return list(request.app.database["carts"].find(limit=100))


