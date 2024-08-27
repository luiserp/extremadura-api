from ollama import Client
import os

class OllamaController:
    
    def __init__(self):
        host = os.getenv("OLLAMA_HOST")
        self.client = Client(host=host)

    def get_description(self, text):
        model_name = 'TextDescriptor'
        return {
            "description": self.client.generate(model=model_name, prompt=text)["response"],
            "model": model_name
        }
