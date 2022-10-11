from fastapi import APIRouter, Body, Request, status
from typing import List

from src.models.users import User, UserAddress
import src.business_objects.user_bo as user_bo

router = APIRouter(prefix="/user",
    tags=["User"])

@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):  
    return user_bo.create_user(request,user)

@router.get("/", response_description="List all users", response_model=List[User])
def list_users(request: Request):
    return user_bo.list_users(request, 100)

@router.get("/{email}", response_description="Get a single user by email", response_model=User)
def find_user(request: Request, email: str):    
    return user_bo.find_user(request, email)

#CLIENTES NÃO SERÃO REMOVIDOS 

#---------------------------------- USER ADDRESS ----------------------------------------------------
@router.post("/address/", response_description="Create a new user address", status_code=status.HTTP_201_CREATED, response_model=UserAddress)
def create_user_address(request: Request, user_addr: UserAddress = Body(...)):   
    return user_bo.create_user_address(request, user_addr)

@router.get("/address/{email}/", response_description="Get user's addresses", response_model=List[UserAddress])
def find_user_address(request: Request, email: str):       
    return user_bo.find_user_address(request, email)

@router.delete("/address/{email}/{addr_id}/", response_description="Delete an address by its id")
def delete_user_addr(request: Request, addr_id: str):
    return user_bo.delete_user_addr(request, addr_id)

