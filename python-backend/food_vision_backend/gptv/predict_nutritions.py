import json

from PIL import Image
from pyprojroot import here

from food_vision_backend.gptv.prompt import prompt
from food_vision_backend.gptv.util import get_openai_image_prediction
from food_vision_backend.schemas.nutrition_info import NutritionInfo


def clean_gpt4_answer(
    text: str,
) -> str:
    """Although we ask for a JSON, GPT4's answer might occasionally contain other things
    than valid JSON. This function tries to clean it up and return a valid JSON."""

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text


def predict_nutritions_form_image(
    image: Image,
) -> NutritionInfo:
    response = get_openai_image_prediction(
        image=image,
        prompt=prompt,
    )

    response = clean_gpt4_answer(response)

    # Not catching errors for now as we should notice if there was an error.
    data = json.loads(response)
    return NutritionInfo(**data)


if __name__ == "__main__":
    print(
        predict_nutritions_form_image(
            Image.open(here("../data/example-images/big-mac.jpg"))
        )
    )
