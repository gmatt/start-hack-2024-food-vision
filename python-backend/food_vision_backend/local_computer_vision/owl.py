from typing import TypedDict

from PIL import Image
from transformers import pipeline


class BoxDict(TypedDict):
    xmin: int
    ymin: int
    xmax: int
    ymax: int


class OwlResultDict(TypedDict):
    score: float
    label: str
    box: BoxDict


class OwlDetector:
    def __init__(self):
        checkpoint = "google/owlv2-base-patch16-ensemble"
        self.detector = pipeline(model=checkpoint, task="zero-shot-object-detection")

    def predict(self, image: Image) -> list[OwlResultDict]:
        predictions = self.detector(
            image,
            candidate_labels=["food", "drink"],
        )
        return predictions
