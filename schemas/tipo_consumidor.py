from pydantic import BaseModel
from typing import List

class TipoConsumidorCreate(BaseModel):
    nome: str
    valor_kwh: float

class TipoConsumidorRead(TipoConsumidorCreate):
    id: int

    class Config:
        from_attributes = True

class TipoConsumidorUpdate(TipoConsumidorCreate):
    ...

class TipoConsumidorReadList(BaseModel):
    tipos_consumidores: List[TipoConsumidorRead]
