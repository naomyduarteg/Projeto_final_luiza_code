import uuid
from pydantic import BaseModel, Field
from typing import List
from src.models.carts_item import CartsItem

class Cart(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")    
    user_id: str   
    products: List[CartsItem] = []
    total_price: float
    quantity_products: int