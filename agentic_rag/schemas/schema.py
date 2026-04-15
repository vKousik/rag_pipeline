from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=1000)
    model: str = Field(default="groq/llama-3.3-70b-versatile")

class AskResponse(BaseModel):
    query: str
    answer: str
    latency: float
    model_used: str