from pydantic import BaseModel

class CartsItemNew(BaseModel):      
    user_id: str
    product_id: str
    quantity: int
    category: str    #choose Buy or Rent
      
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "user_id": "982043ee-a5bf-4f43-88ed-6a69523cfbe5",
                "product_id": "ebbe5ad9-6cb5-4145-9d13-514118382acf",
                "quantity": 2,
                "category": "Rent"
            }
        }
    
    def __getitem__(self, item):
            return getattr(self, item)    
        
        