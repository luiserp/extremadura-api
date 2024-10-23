from ollama import Client
import os
from sklearn.decomposition import PCA
import numpy as np
class OllamaController:
    
    def __init__(self):
        host = os.getenv("OLLAMA_HOST")
        self.client = Client(host=host)
        self.model_name = 'llama3.2'

    def get_description(self, text):
        return {
            "description": self.client.generate(model=self.model_name, prompt=text)["response"],
            "model": self.model_name
        }


    def get_embbeding(self, text):
        return {
            "embeddings": self.client.embed(model=self.model_name, input=text),
        }
        
    def get_normalized_embbeding(self, text, n_components=2):
        embeddings = self.client.embed(model=self.model_name, input=text)["embeddings"]
        embeddings_array = np.array(embeddings)
        embeddings_normalized = PCA(n_components).fit_transform(embeddings)
        return {
            "embeddings": embeddings,
            "embeddings_normalized": embeddings_normalized
        }