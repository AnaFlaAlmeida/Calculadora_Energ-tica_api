from pydantic import BaseModel
from typing import List
from schemas.dependencia import DependenciaReadOne
from schemas.tipo_dispositivo import TipoDispositivoRead
from schemas.unidade_consumidora import UnidadeConsumidoraRead

class DispositivoCreate(BaseModel):
    nome: str
    consumo: float
    uso_diario: float
    tipo: TipoDispositivoRead
    dependencia: DependenciaReadOne
    unidade_consumidora: UnidadeConsumidoraRead

class DispositivoReadOne(DispositivoCreate):
    id: int

    class Config:
        from_attributes = True

class DispositivoUpdate(DispositivoCreate):
    ...

class DispositivoReadList(BaseModel):
    dispositivos: List[DispositivoReadOne]
