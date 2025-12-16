from fastapi import FastAPI
from pydantic import BaseModel
from .model import load_model, generate_response

class PromptRequest(BaseModel):
    prompt: str

app = FastAPI(title="Archibald AI Assistant")

@app.on_event("startup")
async def startup_event():
    # Load the model on startup
    load_model()

@app.get("/")
async def root():
    return {"message": "Archibald AI Assistant is running"}

@app.post("/generate")
async def generate(request: PromptRequest):
    response = generate_response(request.prompt)
    return {"response": response}