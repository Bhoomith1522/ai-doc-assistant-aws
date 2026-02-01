from fastapi import APIRouter, UploadFile, File
import os
from app.services.pdf_extractor import extract_text_from_pdf

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

    return {
        "filename": file.filename,
        "text_length": len(extracted_text),
        "preview": extracted_text[:500],
    }

