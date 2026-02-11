from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_without_file():
    response = client.post("/docs/upload")
    assert response.status_code == 422  # validation error

def test_upload_pdf():
    with open("tests/sample.pdf", "wb") as f:
        f.write(b"%PDF-1.4 test pdf")

    with open("tests/sample.pdf", "rb") as f:
        response = client.post(
            "/docs/upload",
            files={"file": ("sample.pdf", f, "application/pdf")}
        )

    assert response.status_code == 200
    assert "filename" in response.json()
