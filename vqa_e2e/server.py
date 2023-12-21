import requests
from fastapi import FastAPI
from pydantic import BaseModel
from model import VQAModel
from PIL import Image
import io

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()

_model = VQAModel()

class UserRequest(BaseModel):
    input_img : bytes
    input_question : str

@app.get("/predict")
def predict(self, input: UserRequest) -> dict:
    img = Image.open(io.BytesIO(input.input_img))
    return _model.predict(img, input.input_question)