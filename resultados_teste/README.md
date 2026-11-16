# Relatório e Evidências de Validação do Modelo

Este diretório contém os artefatos de validação técnica do modelo de Regressão Logística treinado para a análise preditiva de **Risco de Crédito**.

Todos os testes foram executados sobre o conjunto independente de teste (`X_test`), composto por **200 amostras** originais que não foram apresentadas ao modelo durante a etapa de treinamento (ajuste).

## Conteúdo da Pasta

### 1. 📊 [Matriz de Confusão (matriz_confusao.png)](matriz_confusao.png)
Este gráfico de calor representa os acertos e erros de classificação do algoritmo:
- **Verdadeiros Negativos (Baixo Risco previsto corretamente):** 160 casos
- **Verdadeiros Positivos (Alto Risco previsto corretamente):** 40 casos
- **Falsos Positivos / Falsos Negativos (Classificações incorretas):** 0 casos

Mostra que o modelo separou as duas classes de forma perfeita nesta base de dados simulada.

### 2. 📈 [Curva ROC / AUC (curva_roc.png)](curva_roc.png)
A curva ROC (Receiver Operating Characteristic) ilustra o trade-off entre a taxa de verdadeiros positivos e falsos positivos:
- **Área sob a Curva (AUC):** **1.00**
- O resultado de 1.00 confirma um poder discriminatório excelente, indicando que a probabilidade calculada pela API para clientes de alto risco é consistentemente superior à de clientes com bom perfil de pagamento.

### 3. 📄 [Relatório Oficial de Métricas (relatorio_metricas.txt)](relatorio_metricas.txt)
Contém as métricas quantitativas completas computadas via Scikit-Learn:
- **Acurácia (Accuracy):** 100.00%
- **F1-Score Geral:** 1.00
- **Precisão e Sensibilidade (Recall):** 1.00 para ambas as classes (Baixo Risco e Alto Risco)

---
*Estes resultados comprovam a integridade e prontidão do artefato físico `modelo_risco_credito.joblib` antes de sua publicação na API em ambiente de homologação/produção.*
