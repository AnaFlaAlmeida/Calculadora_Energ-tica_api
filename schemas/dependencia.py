from pydantic import BaseModel
from typing import List
from schemas.unidade_consumidora import UnidadeConsumidoraRead

class DependenciaCreate(BaseModel):
    nome: str
    unidade_consumidora: UnidadeConsumidoraRead

class DependenciaReadOne(DependenciaCreate):
    id: int

    class Config:
        from_attributes = True

class DependenciaUpdate(DependenciaCreate):
    ...

class DependenciaReadList(BaseModel):
    dependencias: List[DependenciaReadOne]
