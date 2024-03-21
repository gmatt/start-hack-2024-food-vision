from dataclasses import dataclass


@dataclass
class NutritionInfo:
    """
    This dataclass holds all the fields to be predicted about the food based on an image
    by the AI models.
    """

    name: str
    """Informal name of food, either generic name, like 'Hamburger' or product name, like 'Milka Milk Chocolate'."""
    quantity: str
    """Either weight in grams, or volume in ml (in case of liquids). Written as e.g. '100g' or '100ml'."""
    calories: float
    """Calories in kcal as float."""
    fat: float
    """Predicted macronutrient content based on food name and quantity, in grams, nutrient: fats."""
    protein: float
    """Predicted macronutrient content based on food name and quantity, in grams, nutrient: proteins."""
    carb: float
    """Predicted macronutrient content based on food name and quantity, in grams, nutrient: carbohydrates."""
