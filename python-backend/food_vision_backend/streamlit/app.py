import inspect

import streamlit as st
from PIL import Image

from food_vision_backend.gptv.predict_nutritions import predict_nutritions_form_image
from food_vision_backend.schemas.nutrition_info import NutritionInfo

file = st.file_uploader(
    "Upload Image of Food or Drink",
    type=["png", "jpg", "jpeg"],
)

if st.button("Predict Nutritions", disabled=not file):
    image = Image.open(file)
    with st.spinner():
        result = predict_nutritions_form_image(image)
    st.write(result)
    st.code(inspect.getsource(NutritionInfo), "python")
