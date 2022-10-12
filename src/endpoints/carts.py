from fastapi import APIRouter, Request, status, Body
from typing import List

from src.models.carts import Cart
from src.models.carts_item_new import CartsItemNew
import src.business_objects.cart_bo as cart_bo

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/",response_description="Get all carts", response_model=List[Cart])
def get_carts(request: Request):    
    return cart_bo.get_all_carts(request, 100)    

@router.get("/{user_id}/",response_description="Get a cart by user id",response_model=Cart)
def get_cart(request: Request,user_id: str):               
    return cart_bo.get_cart(request,user_id)

@router.post("/", response_description="Create and update a cart", status_code=status.HTTP_201_CREATED, response_model=Cart)
def create_cart(request: Request, cartsItemNew: CartsItemNew):
    return cart_bo.create_cart(request, cartsItemNew)
    

@router.delete("/{user_id}/{product_id}", response_description="Delete an item from cart", status_code=status.HTTP_200_OK)
def delete_product(request: Request, user_id: str, product_id: str):    
    return cart_bo.delete_product(request, user_id, product_id)

@router.delete("/{user_id}/", response_description="Delete a cart", status_code=status.HTTP_200_OK)
def delete_cart(request: Request, user_id: str):    
    return cart_bo.delete_cart(request, user_id)