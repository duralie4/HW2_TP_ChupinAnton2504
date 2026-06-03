from Ingredient import Ingredient
from Recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str) -> None:
        for item in self._items:
            if item[1] == title:
                self._items.remove(item)
            else:
                pass

    def get_list(self):
        total = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in total:
                total[key] += ingredient.quantity
            else:
                total[key] = ingredient.quantity
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in total.items()]
        result.sort(key=lambda ing: ing.name)
        return result

    def __add__(self, other: "ShoppingList") -> "ShoppingList":
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list
