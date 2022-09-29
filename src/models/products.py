import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str 
    description: str
    price: float
  
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "55554aa666bb789",
                "name": "Razer BlackShark V2 Gaming Headset",
                "description": "If esports is everything, give it your all with the Razer BlackShark V2.",
                "price": 79.99
            }
        }

class ItemUpdate(BaseModel):
    name: Optional[str] 
    description: Optional[str]
    price: Optional[float]
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Razer BlackShark V2 Gaming Headset",
                "description": "If esports is everything, give it your all with the Razer BlackShark V2.",
                "price": 75
            }
        }
