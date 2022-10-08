from pydantic import BaseModel

class CartsItem(BaseModel):      
    product_id: str
    quantity: int
    price: float
    
    
    def __getitem__(self, item):
        return getattr(self, item)