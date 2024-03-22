import inspect

from food_vision_backend.schemas.nutrition_info import NutritionInfo

# `inspect.getsource(NutritionInfo)` simply adds the source code of the data class,
# so gpt gets all the descriptions, without needing to repeat them here.

prompt = f"""
Based on an image of a food or drink, predict the informal name of the consumable,
predict its weight in g or volume in ml, and predict the macronutrient values.

Answer only with a JSON containing the fields defined below:
{inspect.getsource(NutritionInfo)}
"""
