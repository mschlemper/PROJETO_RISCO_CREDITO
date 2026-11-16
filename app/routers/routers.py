from fastapi import APIRouter, HTTPException, status
from app.schemas.schemas import PredictionInput, PredictionOutput
from app.services.services import PredictorService

router = APIRouter()

try:
    predictor = PredictorService()
    model_loaded = True
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    model_loaded = False

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    if model_loaded:
        return {
            "status": "healthy",
            "database": "connected (simulated)",
            "ml_model_loaded": True
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Serviço instável: O modelo preditivo falhou ao carregar em memória."
        )

@router.post("/predict", response_model=PredictionOutput, status_code=status.HTTP_200_OK)
def get_prediction(payload: PredictionInput):
    if not model_loaded:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="O modelo não está disponível na memória da API."
        )
    try:
        resultado = predictor.predict(
            idade=payload.idade,
            renda_anual=payload.renda_anual,
            historico_inadimplencia=payload.historico_inadimplencia,
            score_credito=payload.score_credito
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno durante a inferência: {str(e)}"
        )
