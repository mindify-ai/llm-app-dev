from fastapi.testclient import TestClient
from index.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"server ok": True}
    
def test_chat():
    response = client.post("/api/chat", data={"user_request": "What is OpenAI?"})
    assert response.status_code == 200
    assert response.json()["result"] != ""