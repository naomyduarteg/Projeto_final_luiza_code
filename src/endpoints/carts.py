from fastapi import APIRouter, Request, HTTPException, status
from typing import List
from src.models.carts import Cart


router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/",response_description="Get all carts", response_model=List[Cart])
def return_cart(request: Request):
    
    return list(request.app.database["carts"].find(limit=100))

@router.get("/{user_id}/",response_description="Get a cart by user id",response_model=Cart)
def return_cart(user_id: str,request: Request):
               
    if (cart := request.app.database["carts"].find_one({"user_id": user_id})) is not None:
        return cart
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cart with user id {user_id} not found")


