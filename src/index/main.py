from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from ai import chatbot

isProduction = True

origins = ["*"]

if isProduction:
    app = FastAPI(
        title="LLM API Endpoints",
        docs_url=None,  # Disable docs (Swagger UI)
        redoc_url=None,  # Disable redoc
    )
else:
    app = FastAPI(title="LLM API Endpoints")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Create a homepage route
@app.get("/")
def index():
    return {"server ok": True}


@app.post("/api/chat")
async def chat(user_request: str = Form(...)):
    """
    Chat with LLM Backend
    """
    # Get the text content in the user request
    result = chatbot(user_request=user_request)

    return {"result": result}
