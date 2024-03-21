import asyncio
import logging
import os

from PIL import Image
from pyprojroot import here

from food_vision_backend.local_computer_vision.owl import OwlDetector

screenshot_path = here("../data/temp/screen.png")

DETECTION_HISTORY_SIZE = 5


def do_macos_screenshot():
    os.system(f"screencapture {screenshot_path}")


class SmartGlassDemo:
    def __init__(self):
        self.local_detector = OwlDetector()
        self.detection_history: list[bool] = [False] * DETECTION_HISTORY_SIZE
        asyncio.create_task(self.tick())

    async def tick(self):
        while True:
            do_macos_screenshot()
            image = Image.open(screenshot_path)
            logging.info("Took screenshot.")
            prediction = self.local_detector.predict(image)
            logging.info(prediction)
            detected = bool(len(prediction))
            # Roll the time series, discard oldest.
            self.detection_history = self.detection_history[1:] + [detected]

            await asyncio.sleep(1)
