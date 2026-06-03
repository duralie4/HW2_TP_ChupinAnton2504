import pytest
from Ingredient import Ingredient
from Recipe import Recipe

def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_eq_of_same_name_and_unit():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 1000.0, "г")
    assert ing1 == ing2

def test_eq_of_diff_names():
    ing1 = Ingredient("Сахар", 500.0, "г")
    ing2 = Ingredient("Мука", 500.0, "г")
    assert ing1 != ing2

def test_eq_of_diff_unit():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 500.0, "кг")
    assert ing1 != ing2

def test_recipe_creation():
    ingredients = [Ingredient("Мука", 500.0, "г")]
    recipe = Recipe("Пицца Маргарита", ingredients)
    assert recipe.title == "Пиццы Маргарита"
    assert recipe.ingredients == ingredients

def test_add_new_ingredient():
    recipe = Recipe("Пицца Маргарита", [])
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 500.0

def test_add_same_ingredient():
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г")])
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 1000.0

def test_scale_returns_new_recipe():
    original = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г")])
    scaled = original.scale(2)
    assert scaled is not original
    assert original.ingredients[0].quantity == 500.0

def test_scale_of_multiple_ings():
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")])
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 1000.0
    assert scaled.ingredients[1].quantity == 200.0

def test_negative_ratio_exception():
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")])
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-3)

def test_len_count_of_unique_ing():
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")])
    assert len(recipe) == 2