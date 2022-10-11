from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder

from src.models.products import Item, ItemUpdate

def get_collection_items(request: Request):
  return request.app.database["items"]

def create_item(request: Request, item: Item):
    item = jsonable_encoder(item)
    new_item = get_collection_items(request).insert_one(item)
    created_item = get_collection_items(request).find_one(
        {"_id": new_item.inserted_id} 
    )

    return created_item
  
def update_item(request: Request, id: str, item: ItemUpdate):
    item = {k: v for k, v in item.dict().items() if v is not None}
    if len(item) >= 1:
        update_result = get_collection_items(request).update_one(
            {"_id": id}, {"$set": item}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")

    if (
        existing_item := get_collection_items(request).find_one({"_id": id})
    ) is not None:
        return existing_item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")
  
def list_items(request: Request, limit: int):
    items = list(get_collection_items(request).find(limit=limit))
    return items
  
def list_items_by_id(request: Request, id: str):
    if (item := get_collection_items(request).find_one({"_id": id})) is not None:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")
  
def list_items_by_name(request: Request, name: str):
    if (item := get_collection_items(request).find_one({"name": name})) is not None:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with name {name} not found")
  
def delete_item(request: Request, id: str):
    deleted_item = get_collection_items(request).delete_one({"_id": id})

    if deleted_item.deleted_count == 1:
        return f"Item with ID {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")