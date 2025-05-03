from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models
import schemas

router = APIRouter()

@router.post("/refeicoes/", response_model=schemas.Refeicao)
def criar_refeicao(refeicao: schemas.RefeicaoCreate, db: Session = Depends(get_db)):
    db_refeicao = models.Refeicao(**refeicao.model_dump())
    db.add(db_refeicao)
    db.commit()
    db.refresh(db_refeicao)
    return db_refeicao

@router.get("/refeicoes/", response_model=List[schemas.Refeicao])
def listar_refeicoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    refeicoes = db.query(models.Refeicao).offset(skip).limit(limit).all()
    return refeicoes

@router.get("/refeicoes/{refeicao_id}", response_model=schemas.Refeicao)
def obter_refeicao(refeicao_id: int, db: Session = Depends(get_db)):
    refeicao = db.query(models.Refeicao).filter(models.Refeicao.id == refeicao_id).first()
    if refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    return refeicao

@router.put("/refeicoes/{refeicao_id}", response_model=schemas.Refeicao)
def atualizar_refeicao(refeicao_id: int, refeicao: schemas.RefeicaoCreate, db: Session = Depends(get_db)):
    db_refeicao = db.query(models.Refeicao).filter(models.Refeicao.id == refeicao_id).first()
    if db_refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    
    for key, value in refeicao.model_dump().items():
        setattr(db_refeicao, key, value)
    
    db.commit()
    db.refresh(db_refeicao)
    return db_refeicao

@router.delete("/refeicoes/{refeicao_id}")
def deletar_refeicao(refeicao_id: int, db: Session = Depends(get_db)):
    db_refeicao = db.query(models.Refeicao).filter(models.Refeicao.id == refeicao_id).first()
    if db_refeicao is None:
        raise HTTPException(status_code=404, detail="Refeição não encontrada")
    
    db.delete(db_refeicao)
    db.commit()
    return {"message": "Refeição deletada com sucesso"} 