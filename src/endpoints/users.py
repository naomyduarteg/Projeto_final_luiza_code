from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from src.models.users import User, UserAddress 
from bson import ObjectId

router = APIRouter(prefix="/user",
    tags=["User"])

@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user

@router.get("/", response_description="List all users", response_model=List[User])
def list_users(request: Request):
    users = list(request.app.database["users"].find(limit=100))
    return users

@router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(id: str, request: Request):
    if (user := request.app.database["users"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")


@router.delete("/{id}", response_description="Delete a user")
def delete_user(id: str, request: Request, response: Response):
    deleted_user = request.app.database["users"].delete_one({"_id": id})

    if deleted_user.deleted_count == 1:
        return f"User with ID {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")

#---------------------------------- USER ADDRESS ----------------------------------------------------
@router.post("/address/", response_description="Create a new user address", status_code=status.HTTP_201_CREATED, response_model=UserAddress)
def create_user_address(request: Request, user_addr: UserAddress = Body(...)):
    user_addr = jsonable_encoder(user_addr)
    new_addr = request.app.database["addresses"].insert_one(user_addr)
    created_addr = request.app.database["addresses"].find_one(
        {"_id": new_addr.inserted_id} 
    )

    return created_addr

@router.get("/address/{user_id}/", response_description="Get user's addresses", response_model=List[UserAddress])
def find_user_address(user_id: str, request: Request):
    user_addrs = list(request.app.database["addresses"].find({"user_id": user_id}))
    return user_addrs

@router.delete("/address/{user_id}/{addres_id}/", response_description="Delete an address by its id")
def delete_user_addr(addr_id: str, request: Request, response: Response):
    deleted_user_addr = request.app.database["addresses"].delete_one({"_id": ObjectId(addr_id)})

    if deleted_user_addr.deleted_count == 1:
        return f"Address with ID {addr_id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address with ID {addr_id} not found")


