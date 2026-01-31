from fastapi import FastAPI
from pydantic import BaseModel

from app.api.routes_chat import router as chat_router

app = FastAPI(title="AI Doc Assistant API")


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok", "service": "ai-doc-assistant"}


app.include_router(chat_router)
