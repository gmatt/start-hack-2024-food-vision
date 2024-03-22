import asyncio
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from PIL import Image
from pyprojroot import here

from food_vision_backend.gpt4_vision.predict_nutritions import (
    predict_nutritions_form_image,
)
from food_vision_backend.gpt4_vision.util import get_openai_image_prediction
from food_vision_backend.local_computer_vision.owl import OwlDetector
from food_vision_backend.schemas.nutrition_info import NutritionInfo

screenshots_path = here("../data/temp/")

DETECTION_HISTORY_SIZE = 5


def do_macos_screenshot(path: Path):
    os.system(f"screencapture {path}")


class SmartGlassDemo:
    def __init__(self):
        self.local_detector = OwlDetector()
        self.detection_history: list[bool] = [False] * DETECTION_HISTORY_SIZE
        asyncio.create_task(self.detection_loop())
        self.last_nutrition_prediction: Optional[NutritionInfo] = None

    async def detection_loop(self):
        while True:
            # This demo is specific for screen sharing, but could work with arbitrary
            # image input.
            do_macos_screenshot(
                screenshots_path / f"screenshot_{datetime.now().isoformat()}.png"
            )
            logging.info("Took screenshot.")
            # For debugging, we keep all screenshots, but the last 3 would be enough.
            image = Image.open(sorted(screenshots_path.glob("*.png"))[-1])
            prediction = self.local_detector.predict(image)
            logging.info(prediction)
            detected = bool(len(prediction))
            # Roll the time series, discard oldest.
            self.detection_history = self.detection_history[1:] + [detected]

            # If it's a new food in a while, we save its photo, in case the user eats
            # it.
            if self.detection_history[-3:] == [False, False, True]:
                image.save(here("../data/temp/a_last_milestone.png"))
                image.convert("RGB").save(
                    here("../react-frontend/public/a_last_milestone.jpg")
                )

            if self.detection_history[-2] and not self.detection_history[-1]:
                last_3_images = [
                    Image.open(image)
                    for image in sorted(screenshots_path.glob("*.png"))[-3:]
                ]
                print(last_3_images)
                # plt.imshow(last_3_images[0])
                # plt.show()
                # plt.imshow(last_3_images[1])
                # plt.show()
                # plt.imshow(last_3_images[2])
                # plt.show()
                end_predicted = self.predict_end_of_meal(last_3_images)
                if end_predicted:
                    predicted_nutritions = predict_nutritions_form_image(
                        Image.open(here("../data/temp/a_last_milestone.png"))
                    )
                    self.last_nutrition_prediction = predicted_nutritions
                    # Wait for frontend to poll, then reset.
                    await asyncio.sleep(5)
                    self.last_nutrition_prediction = None

            # Recognition takes several seconds as of now, so a shorter sleep is fine.
            await asyncio.sleep(1)

    @staticmethod
    def predict_end_of_meal(images: list[Image]) -> bool:
        answer = get_openai_image_prediction(
            images=images,
            prompt="""Have this person finished eating or drinking their current meal
based on the last 3 snapshots? Answer with 'yes' or 'no' only. Note that the video can
either be from first person or third person perspective.""",
        )
        if answer.lower().startswith("no"):
            return False
        elif answer.lower().startswith("yes"):
            return True
        else:
            raise ValueError("Can't parse answer form ChatGPT.")
