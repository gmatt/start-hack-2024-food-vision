import base64
import logging
import os
from io import BytesIO
from typing import Optional

import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def pil_to_base64(
    image: Image,
) -> str:
    """
    Converts Pillow image to base64 encoded string.
    """
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def get_openai_image_prediction(
    images: list[Image],
    prompt: str,
    max_tokens: Optional[int] = None,
) -> str:
    """
    Given a PIL image and a text prompt, gets answer from OpenAI GPT4 vision API.

    Requires `OPENAI_API_KEY` envvar to be set, or defined in `.env`.
    """

    # Source:
    # https://platform.openai.com/docs/guides/vision/multiple-image-inputs
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    *(
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{pil_to_base64(image)}"
                            },
                        }
                        for image in images
                    ),
                ],
            }
        ],
        **({"max_tokens": max_tokens} if max_tokens else {}),
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    logging.info(response.text)

    return response.json()["choices"][0]["message"]["content"]
