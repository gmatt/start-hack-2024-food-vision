import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from pyprojroot import here
from transformers import pipeline

checkpoint = "google/owlv2-base-patch16-ensemble"
detector = pipeline(model=checkpoint, task="zero-shot-object-detection")

image = Image.open(here("../data/example-images/big-mac.jpg"))

predictions = detector(
    image,
    candidate_labels=["food", "drink"],
)

draw = ImageDraw.Draw(image)

for prediction in predictions:
    box = prediction["box"]
    label = prediction["label"]
    score = prediction["score"]

    xmin, ymin, xmax, ymax = box.values()
    draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=1)
    draw.text((xmin, ymin), f"{label}: {round(score,2)}", fill="white")

plt.imshow(np.asarray(image))
plt.show()
