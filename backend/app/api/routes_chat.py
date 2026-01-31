from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    reply_text = f"Hello {payload.user_id}, you said: {payload.message}"
    return ChatResponse(reply=reply_text)
