from Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients if ingredients is not None else [])
        self.diet_type = diet_type

    def scale(self, ratio: float) -> "DietaryRecipe":
        super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, self.ingredients)

    def __str__(self) -> str:
        return f"[{self.diet_type}] " + super().__str__()