import joblib
import numpy as np
import os

class PredictorService:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), '../../models/modelo_risco_credito.joblib')
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Artefato do modelo não encontrado em: {self.model_path}")

        artefatos = joblib.load(self.model_path)
        self.model = artefatos['model']
        self.scaler = artefatos['scaler']

    def predict(self, idade: int, renda_anual: float, historico_inadimplencia: int, score_credito: int):
        # Preparar dados de entrada
        features = np.array([[idade, renda_anual, historico_inadimplencia, score_credito]])
        features_scaled = self.scaler.transform(features)

        # Realizar predição
        predicao = int(self.model.predict(features_scaled)[0])
        probabilidade = float(self.model.predict_proba(features_scaled)[0][1])

        mensagem = "Crédito Aprovado / Baixo Risco" if predicao == 0 else "Crédito em Análise / Alto Risco"

        return {
            "classe_predicao": predicao,
            "probabilidade_alto_risco": probabilidade,
            "mensagem": mensagem
        }
