from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=5, max_length=1000)


class ChatResponse(BaseModel):
    response: str
    status: str = "success"
