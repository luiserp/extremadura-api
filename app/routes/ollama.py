from controllers.ollama.ollama_controller import OllamaController
from pydantic import BaseModel
from typing import Annotated
from fastapi import Body

class Input(BaseModel):
    text: str

# Ollama Module Router
def router(app):
    
    # Description
    @app.post("/description")
    def description(input: Input):
        return OllamaController().get_description(input.text)
