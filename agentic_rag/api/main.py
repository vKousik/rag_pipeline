from fastapi import FastAPI, HTTPException
from schemas.schema import AskRequest, AskResponse
from services.rag_services import get_answer, SYSTEM_PROMPT
from mlflow_utills.tracker import track_run

app = FastAPI(title="Agentic RAG API 🚀")

@app.get("/")
def home():
    return {"message": "RAG API running"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        def run():
            return get_answer(req.query)

        answer, latency = track_run(
            query=req.query,
            model=req.model,
            system_prompt=SYSTEM_PROMPT,
            func=run
        )

        return AskResponse(
            query=req.query,
            answer=answer,
            latency=latency,
            model_used=req.model
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))