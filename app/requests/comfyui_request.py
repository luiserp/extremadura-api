from pydantic import BaseModel

class Input(BaseModel):
    text: str
    seed: int = 0
