import pandas as pd
from PIL import Image
from pyprojroot import here
from tqdm.auto import tqdm

from food_vision_backend.gpt4_vision.predict_nutritions import (
    predict_nutritions_form_image,
)

data = []

for file in tqdm(list(here("../data/nutrition5k/").glob("dish_*.png"))):
    n = predict_nutritions_form_image(Image.open(file))

    data.append(
        {
            "dish_id": file.stem,
            "calories": n.calories,
            "mass": float(n.quantity.replace("g", "")),
            "fat": n.fat,
            "carb": n.carb,
            "protein": n.protein,
        }
    )

df = pd.DataFrame(data)
df.to_csv(
    here("food_vision_backend/eval/res.csv"),
    index=False,
    header=False,
)
