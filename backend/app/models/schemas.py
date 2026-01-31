from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: str = Field(..., examples=["u123"])
    message: str = Field(..., min_length=1, examples=["Hello"])


class ChatResponse(BaseModel):
    reply: str
