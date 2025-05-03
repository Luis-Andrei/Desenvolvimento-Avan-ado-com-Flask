from fastapi import FastAPI
from database import engine, Base
import routes

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Daily Diet API")

# Incluir as rotas
app.include_router(routes.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Bem-vindo à Daily Diet API"} 