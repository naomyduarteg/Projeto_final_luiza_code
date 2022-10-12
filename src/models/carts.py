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
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
             "example": {                
                "user_id": "ad7302a5-cc2b-4afb",
                "products": [
                    {
                        "product_id": "47694f4f-1eea-4092",
                        "quantity": 2,
                        "price": 6.0
                    }
                ],
                "total_price": 12.0,
                "quantity_products": 2

            }
        }