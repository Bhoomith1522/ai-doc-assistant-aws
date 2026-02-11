from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_without_docs():
    response = client.post("/chat", json={"query": "hello"})
    assert response.status_code == 200
    assert "warning" in response.json()

def test_chat_query():
    response = client.post("/chat", json={"query": "test"})
    assert response.status_code == 200
    assert "query" in response.json()
