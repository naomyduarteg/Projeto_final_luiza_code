import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    type: str 
    name: str 
    description: str
    price_rent: float
    price_buy: float
    genre: str
    year: int 
    duration: Optional[float] #em minutos
    languages: str 
    subtitles: str

  
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "55554aa666bb789",
                "type": "Filme",
                "name": "Bacurau",
                "description": "Pouco após a morte de dona Carmelita, aos 94 anos, os moradores de um pequeno povoado \
                localizado no sertão brasileiro, chamado Bacurau, descobrem que a comunidade não consta mais em qualquer \
                mapa. Aos poucos, percebem algo estranho na região: enquanto drones passeiam pelos céus, estrangeiros chegam\
                à cidade pela primeira vez. Quando carros se tornam vítimas de tiros e cadáveres começam a aparecer, Teresa \
                (Bárbara Colen), Domingas (Sônia Braga), Acácio (Thomas Aquino), Plínio (Wilson Rabelo), Lunga (Silvero Pereira)\
                e outros habitantes chegam à conclusão de que estão sendo atacados. Falta identificar o inimigo e criar coletivamente\
                um meio de defesa",
                "price_rent": 11.90,
                "price_buy": 22.90,
                "genre": "Drama, Suspense",
                "year": 2019,
                "duration": 171,
                "languages": "Português",
                "subtitles": "Inglês"
            }
        }

class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price_rent: Optional[float]
    price_buy: Optional[float]
    genre: Optional[str]
    year: Optional[int]
    duration: Optional[float]
    languages: Optional[str]
    subtitles: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "price_rent": 10.90,
                "price_buy": 20.90,
                "duration": 42,
                "languages": "Português",
                "subtitles": "Português" 
            }
        }
        
class ItemNew(BaseModel):
    type: str 
    name: str 
    description: str
    price_rent: float
    price_buy: float
    genre: str
    year: int 
    duration: Optional[float] #em minutos
    languages: str 
    subtitles: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
             "example": {                
                "type": "Filme",
                "name": "Bacurau",
                "description": "Pouco após a morte de dona Carmelita, aos 94 anos, os moradores de um pequeno povoado \
                localizado no sertão brasileiro, chamado Bacurau, descobrem que a comunidade não consta mais em qualquer \
                mapa. Aos poucos, percebem algo estranho na região: enquanto drones passeiam pelos céus, estrangeiros chegam\
                à cidade pela primeira vez. Quando carros se tornam vítimas de tiros e cadáveres começam a aparecer, Teresa \
                (Bárbara Colen), Domingas (Sônia Braga), Acácio (Thomas Aquino), Plínio (Wilson Rabelo), Lunga (Silvero Pereira)\
                e outros habitantes chegam à conclusão de que estão sendo atacados. Falta identificar o inimigo e criar coletivamente\
                um meio de defesa",
                "price_rent": 11.90,
                "price_buy": 22.90,
                "genre": "Drama, Suspense",
                "year": 2019,
                "duration": 171,
                "languages": "Português",
                "subtitles": "Inglês"
            }
        }
