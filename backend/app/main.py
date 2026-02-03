from fastapi import FastAPI,Request
from pydantic import BaseModel
from app.api.routes_chat import router as chat_router
from app.api.routes_docs import router as docs_router
from app.api.routes_debug import router as debug_router
from app.core.logging import setup_logging

import time
import logging


setup_logging()

app = FastAPI(title="AI Doc Assistant API")

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    import time
    import logging

    logger = logging.getLogger("app")

    start_time = time.time()

    # call next handler
    response = await call_next(request)

    process_time = time.time() - start_time
    logger.info(
        f"{request.method} {request.url.path} completed in {process_time:.3f}s"
    )

    return response

from fastapi.responses import JSONResponse


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    import logging
    logger = logging.getLogger("app")

    logger.error(f"Unhandled error: {exc}")

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )

class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok", "service": "ai-doc-assistant"}


app.include_router(chat_router)
app.include_router(docs_router)
app.include_router(debug_router)


