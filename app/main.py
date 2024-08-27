from typing import Union
from fastapi import FastAPI
from routes.ollama import router as ollama_router
from routes.comfyui import router as comfyui_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

ollama_router(app)
comfyui_router(app)