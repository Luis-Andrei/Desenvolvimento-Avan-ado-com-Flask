from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class Refeicao(Base):
    __tablename__ = "refeicoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    data_hora = Column(DateTime, default=datetime.utcnow)
    dentro_da_dieta = Column(Boolean, default=True) 