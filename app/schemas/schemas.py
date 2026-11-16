from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    idade: int = Field(..., ge=18, le=100, description="Idade do solicitante do crédito (mínimo 18 anos)")
    renda_anual: float = Field(..., gt=0, description="Renda anual do solicitante em valores positivos")
    historico_inadimplencia: int = Field(..., ge=0, le=1, description="0 para histórico limpo, 1 para histórico com inadimplência")
    score_credito: int = Field(..., ge=300, le=850, description="Score de crédito variando de 300 a 850")

    class Config:
        json_schema_extra = {
            "example": {
                "idade": 35,
                "renda_anual": 55000.0,
                "historico_inadimplencia": 0,
                "score_credito": 720
            }
        }

class PredictionOutput(BaseModel):
    classe_predicao: int = Field(..., description="Classe predita: 0 para Baixo Risco, 1 para Alto Risco")
    probabilidade_alto_risco: float = Field(..., description="Probabilidade estimada do solicitante ser alto risco")
    mensagem: str = Field(..., description="Mensagem descritiva do resultado")
