from pydantic import BaseModel
from typing import List
from schemas.tipo_consumidor import TipoConsumidorRead

class UnidadeConsumidoraCreate(BaseModel):
    nome: str
    tipo: TipoConsumidorRead

class UnidadeConsumidoraRead(UnidadeConsumidoraCreate):
    id: int

    class Config:
        from_attributes = True

class UnidadeConsumidoraUpdate(UnidadeConsumidoraCreate):
    ...

class UnidadeConsumidoraReadList(BaseModel):
    unidades_consumidoras: List[UnidadeConsumidoraRead]
