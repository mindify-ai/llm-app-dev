from fastapi.testclient import TestClient
from index.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"server ok": True}
    
def test_gpt_chat():
    response = client.post("/api/chat/gpt3", data={"user_request": "What is OpenAI?"})
    assert response.status_code == 200
    assert response.json()["result"] != ""
    
def test_llama_chat():
    response = client.post("/api/chat/llama", data={"user_request": "What is LLM?"})
    assert response.status_code == 200
    assert response.json()["result"] != ""