from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RefeicaoBase(BaseModel):
    nome: str
    descricao: str
    data_hora: Optional[datetime] = None
    dentro_da_dieta: bool = True

class RefeicaoCreate(RefeicaoBase):
    pass

class Refeicao(RefeicaoBase):
    id: int

    class Config:
        orm_mode = True 