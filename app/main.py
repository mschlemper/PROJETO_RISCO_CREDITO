from fastapi import FastAPI
from app.routers.routers import router as api_router

app = FastAPI(
    title="API de Análise Preditiva de Risco de Crédito",
    description="API REST criada com FastAPI para inferência sob demanda do modelo de Machine Learning.",
    version="1.0.0"
)

# Registrar as rotas da nossa aplicação modular
app.include_router(api_router, prefix="/v1")

@app.get("/")
def root():
    return {"mensagem": "API de Análise Preditiva Rodando. Acesse /docs para ver a documentação interativa Swagger!"}
