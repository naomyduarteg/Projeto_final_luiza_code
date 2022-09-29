from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from src.models.products import Item, ItemUpdate
from bson import ObjectId

router = APIRouter(prefix="/item",
    tags=["Item"])

@router.post("/", response_description="Create an item", status_code=status.HTTP_201_CREATED, response_model=Item)
def create_item(request: Request, item: Item):
    item = jsonable_encoder(item)
    new_item = request.app.database["items"].insert_one(item)
    created_item = request.app.database["items"].find_one(
        {"_id": new_item.inserted_id} 
    )

    return created_item

@router.put("/{id}", response_description="Update an item", response_model=Item)
def update_item(id: str, request: Request, item: ItemUpdate = Body(...)):
    item = {k: v for k, v in item.dict().items() if v is not None}
    if len(item) >= 1:
        update_result = request.app.database["items"].update_one(
            {"_id": id}, {"$set": item}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")

    if (
        existing_item := request.app.database["items"].find_one({"_id": id})
    ) is not None:
        return existing_item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")

@router.get("/", response_description="List all items", response_model=List[Item])
def list_items(request: Request):
    items = list(request.app.database["items"].find(limit=100))
    return items

@router.delete("/{id}", response_description="Delete an item")
def delete_item(id: str, request: Request, response: Response):
    deleted_item = request.app.database["items"].delete_one({"_id": id})

    if deleted_item.deleted_count == 1:
        return f"Item with ID {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")