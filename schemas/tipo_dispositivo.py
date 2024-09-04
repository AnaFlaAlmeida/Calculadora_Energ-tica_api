from pydantic import BaseModel
from typing import List

class TipoDispositivoCreate(BaseModel):
    nome: str

class TipoDispositivoRead(TipoDispositivoCreate):
    id: int

    class Config:
        from_attributes = True

class TipoDispositivoUpdate(TipoDispositivoCreate):
    ...

class TipoDispositivoReadList(BaseModel):
    tipos_dispositivos: List[TipoDispositivoRead]
