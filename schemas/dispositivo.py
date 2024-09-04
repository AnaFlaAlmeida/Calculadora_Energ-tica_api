from pydantic import BaseModel, Field

class DispositivoCreate(BaseModel):
    residencia_id: int
    comodo_id: int
    nome: str
    potencia: int = Field(..., gt=0)
    uso_diario: float = Field(..., ge=0, le=24)
