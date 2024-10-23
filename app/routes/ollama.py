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
    
    @app.post("/embbeding")
    def embbeding(input: Input):
        return OllamaController().get_embbeding(input.text)
    

    @app.post("/normalized_embbeding")
    def normalized_embbeding(input: Input):
        return OllamaController().get_normalized_embbeding(input.text, input.n_components if hasattr(input, 'n_components') else 1)
