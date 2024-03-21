import io
from contextlib import asynccontextmanager

from PIL import Image
from fastapi import FastAPI, File, UploadFile

from food_vision_backend.local_computer_vision.owl import OwlDetector

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models["owl"] = OwlDetector()
    yield
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    request_object_content = await image.read()
    img = Image.open(io.BytesIO(request_object_content))
    result = ml_models["owl"].predict(img)
    return {"result": result}
