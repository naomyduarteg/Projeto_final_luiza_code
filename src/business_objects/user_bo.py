from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from src.models.users import UserNew, UserAddress

def get_collection_users(request: Request):
  return request.app.database["users"]

def get_collection_addresses(request: Request):
  return request.app.database["addresses"]

def create_user(request: Request, user: UserNew = Body(...)):
    user = jsonable_encoder(user)
    new_user = get_collection_users(request).insert_one(user)
    created_user = get_collection_users(request).find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user

def list_users(request: Request, limit: int):
    users = list(get_collection_users(request).find(limit = limit))
    return users

def find_user(request: Request, email: str):
    if (user := get_collection_users(request).find_one({"email": email})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email {email} not found")
  
def create_user_address(request: Request, user_addr: UserAddress = Body(...)):
    user_addr = jsonable_encoder(user_addr)
    new_addr = get_collection_addresses(request).insert_one(user_addr)
    created_addr = get_collection_addresses(request).find_one(
        {"_id": new_addr.inserted_id} 
    )

    return created_addr

def find_user_address(request: Request,email: str):
    user_addrs = list(get_collection_addresses(request).find({"user_email": email}))
    if len(user_addrs):
        return user_addrs
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User has no address yet.")
  
def delete_user_addr(request: Request, addr_id: str):
    deleted_user_addr = get_collection_addresses(request).delete_one({"_id": addr_id})

    if deleted_user_addr.deleted_count == 1:
        return f"Address with ID {addr_id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address with ID {addr_id} not found") 