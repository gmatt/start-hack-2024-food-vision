import logging
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from food_vision_backend.smart_glass_demo.main import SmartGlassDemo


class DemoState(BaseModel):
    predictionHistory: list[bool]


demo: Optional[SmartGlassDemo] = None


@asynccontextmanager
async def lifespan(_app: FastAPI):
    global demo

    demo = SmartGlassDemo()
    yield
    demo = None


logging.basicConfig(level=logging.DEBUG)
app = FastAPI(lifespan=lifespan)


@app.get("/getState")
async def get_state() -> DemoState:
    return DemoState(
        predictionHistory=demo.detection_history,
    )
