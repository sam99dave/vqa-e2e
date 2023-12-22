from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from model import VQAModel
from PIL import Image
import io
import numpy as np

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()

_model = VQAModel()

class UserRequest(BaseModel):
    input_question : str

def convert_np_float32_to_float(obj):
    if isinstance(obj, np.float32):
        return float(obj)
    elif isinstance(obj, dict):
        return {key: convert_np_float32_to_float(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_np_float32_to_float(item) for item in obj]
    return obj

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/predict")
# def predict(self, input: UserRequest) -> dict:
#     img = Image.open(io.BytesIO(input.input_img))
#     res = _model.predict(img, input.input_question)
#     print(f'res: {res}')
#     return res

@app.post("/predict/")
def predict(input: UserRequest):
    print(f'input: {input.input_question}')
    res = _model.predict(input.input_question)
    return convert_np_float32_to_float(res)