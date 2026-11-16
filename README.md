# API de Análise Preditiva de Risco de Crédito

## 1. Resumo do Projeto
Esta API foi desenvolvida para atender à Situação de Aprendizagem de Desenvolvimento de IA para Análise Preditiva. O sistema disponibiliza um modelo treinado de Machine Learning para a classificação de Risco de Crédito com alta precisão e baixíssima latência.

## 2. Tecnologias Utilizadas
- **FastAPI**: Framework web moderno e assíncrono para construção de APIs.
- **Pydantic**: Validação de tipos rigorosa na entrada e saída.
- **Scikit-Learn**: Treinamento, escala e pré-processamento do pipeline preditivo.
- **Joblib**: Persistência do modelo físico em disco.
- **Uvicorn**: Servidor ASGI para produção.

## 3. Estrutura de Pastas
```bash
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   └── routers.py
│   ├── schemas/
│   │   └── schemas.py
│   └── services/
│       └── services.py
├── models/
│   └── modelo_risco_credito.joblib
├── requirements.txt
└── README.md
```

## 4. Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/mschlemper/PROJETO_RISCO_CREDITO.git
   cd PROJETO_RISCO_CREDITO
   ```
2. Crie e ative o ambiente virtual (venv):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   # ou
   .\venv\Scripts\activate  # No Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Acesse a documentação gerada de forma automática pelo Swagger em: `http://127.0.0.1:8000/docs`

## 5. Exemplos de Payload (Endpoints)

### `GET /v1/health`
Retorna o status atual da API e do carregamento do modelo.

### `POST /v1/predict`
Recebe os dados do cliente e responde se há classificação de risco alto ou baixo.
**Corpo de Envio (JSON):**
```json
{
  "idade": 35,
  "renda_anual": 55000.0,
  "historico_inadimplencia": 0,
  "score_credito": 720
}
```
**Resposta da API:**
```json
{
  "classe_predicao": 0,
  "probabilidade_alto_risco": 0.1234,
  "mensagem": "Crédito Aprovado / Baixo Risco"
}
```

## 6. Evidências do Projeto
- **Link do Vídeo Demonstrativo**: [Insira o link do seu vídeo no Google Drive aqui]
