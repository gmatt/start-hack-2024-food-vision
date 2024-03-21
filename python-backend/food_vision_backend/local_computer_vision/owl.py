from PIL import Image
from transformers import pipeline


class OwlDetector:
    def __init__(self):
        checkpoint = "google/owlv2-base-patch16-ensemble"
        self.detector = pipeline(model=checkpoint, task="zero-shot-object-detection")

    def predict(self, image: Image):
        predictions = self.detector(
            image,
            candidate_labels=["food", "drink"],
        )
        return predictions
