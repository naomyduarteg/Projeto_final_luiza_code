from pydantic import BaseModel

class CartsItemNew(BaseModel):      
    user_id: str
    product_id: str
    quantity: int
    category: str    
   
    def __getitem__(self, item):
        return getattr(self, item)