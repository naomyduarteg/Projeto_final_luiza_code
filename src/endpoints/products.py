from fastapi import APIRouter, Request, status
from typing import List

from src.models.products import Item, ItemUpdate
import src.business_objects.product_bo as product_bo


router = APIRouter(prefix="/item",
    tags=["Item"])

@router.post("/", response_description="Create an item", status_code=status.HTTP_201_CREATED, response_model=Item)
def create_item(request: Request, item: Item):    
    return product_bo.create_item(request, item)

@router.put("/{id}", response_description="Update an item", response_model=Item)
def update_item(request: Request, id: str, item: ItemUpdate):
    return product_bo.update_item(request, id, item)

@router.get("/", response_description="List all items", response_model=List[Item])
def list_items(request: Request):    
    return product_bo.list_items(request, 100)

@router.get("/{id}/", response_description="List items by id", response_model=Item)
def list_items_by_id(request: Request, id: str):
    return product_bo.list_items_by_id(request, id)

@router.get("/name/{name}/", response_description="List items by name", response_model=Item)
def list_items_by_name(request: Request, name: str):    
    return product_bo.list_items_by_name(request, name)

@router.delete("/{id}/", response_description="Delete an item")
def delete_item(request: Request, id: str):
    return product_bo.delete_item(request, id)