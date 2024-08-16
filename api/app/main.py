from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .ai.chatbot import gpt_chatbot, llama_chatbot

isProduction = False

origins = ["*"]

if isProduction:
    app = FastAPI(
        title="LLM API Endpoints",
        docs_url=None,  # Disable docs (Swagger UI)
        redoc_url=None,  # Disable redoc
    )
    #app.mount("/static", StaticFiles(directory="static"), name="static")
else:
    app = FastAPI(title="LLM API Endpoints")
    #app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Create a homepage route
@app.get("/")
async def index():
    return {"server ok": True}


@app.post("/api/chat/gpt4o/mini", tags=["OpenAI GPT-4o mini"])
async def gpt_chat(user_request: str = Form(...)):
    """
    Chat with LLM Backend - GPT-4o mini
    """
    # Get the text content in the user request
    result = gpt_chatbot(user_request=user_request)

    return {"result": result}


@app.post("/api/chat/llama", tags=["Llama 2 7B Chat"])
async def llama_chat(user_request: str = Form(...)):
    """
    Chat with LLM Backend - Llama 2 7b Chat
    """
    # Get the text content in the user request
    result = llama_chatbot(user_request=user_request)

    return {"result": result}
