import uuid
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str 
    email: EmailStr = Field(unique=True, index=True)
    password: str 

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "4815162342",
                "name": "Dolly",
                "email": "dollyna@gmail.com",
                "password": "cachorrinha.fofa.123"
            }
        }

#-------------------------------- ADDRESS -------------------------------------------
class UserAddress(BaseModel):
    user_id: str 
    street: str 
    city: str  
    state: str
    cep : str 
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": "4815162342",
                "street": "Rua Capitão José Esteves Júnior, 639",
                "city": "Altinópolis",
                "state": "São Paulo",
                "cep": "14350000"
            }
        }