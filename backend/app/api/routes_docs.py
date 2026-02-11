from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_extractor import extract_text_from_pdf
from app.services.text_splitter import split_text
from app.services.embedding import embed_texts
from app.services.vector_store import vector_store

router = APIRouter(tags=["documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/docs/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = ""

    if file.filename.lower().endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)

    chunks = split_text(extracted_text)
    embeddings = embed_texts(chunks)
    metadata = [{"source": file.filename} for _ in chunks]
    vector_store.add(embeddings, chunks, metadata)

    

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "stored": True
    }


