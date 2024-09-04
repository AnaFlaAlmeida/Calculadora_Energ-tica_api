from pydantic import BaseModel
from typing import List

class BandeiraCreate(BaseModel):
    nome: str
    tarifa: float

class BandeiraRead(BandeiraCreate):
    id: int

    class Config:
        from_attributes = True

class BandeiraUpdate(BandeiraCreate):
    ...

class BandeiraReadList(BaseModel):
    bandeiras: List[BandeiraRead]
