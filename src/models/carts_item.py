from pydantic import BaseModel

class CartsItem(BaseModel):      
    product_id: str
    quantity: int
    