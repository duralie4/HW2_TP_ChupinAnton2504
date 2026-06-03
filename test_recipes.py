import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList

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

def test_add_recipe():
    sl = ShoppingList()
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                        Ingredient("Сыр", 100.0, "г")])
    sl.add_recipe(recipe, 1)
    assert len(sl._items) == 1
    assert sl._items[0][0].name == "Мука"
    assert sl._items[0][1] == "Пицца Маргарита"

def test_negative_portions_exception():
    sl = ShoppingList()
    recipe = Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                        Ingredient("Сыр", 100.0, "г")])
    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)
    with pytest.raises(ValueError):
        sl.add_recipe(recipe, -4)

def test_remove_recipe_ingredients():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")]), 1)
    sl.add_recipe(Recipe("Летний салатик", [Ingredient("Огурцы", 200.0, "г"),
                                          Ingredient("Помидоры", 200.0, "г"),
                                          Ingredient("Лук репчатый", 100.0, "г")]), 1)
    sl.remove_recipe("Пиццы Маргарита")
    assert len(sl._items) == 1
    assert sl._items[0][1] == "Летний салатик"

def test_remove_not_existed_recipe():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")]), 1)
    sl.remove_recipe("Суп")
    assert len(sl._items) == 1

def test_get_list_sum_of_same_ings():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Пицца Маргарита", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г")]), 1)
    sl.add_recipe(Recipe("Пицца Песто", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г"),
                                         Ingredient("Соус Песто", 50.0, "г")]), 1)
    result = sl.get_list()
    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 1000.0

def test_returned_list_sorted_by_name():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Пицца Песто", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г"),
                                         Ingredient("Соус Песто", 50.0, "г")]), 1)
    result = sl.get_list()
    names = [ing.name for ing in result]
    assert names == sorted(names)

def test_add_combines():
    sl1 = ShoppingList()
    sl1.add_recipe(Recipe("Пицца Песто", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г"),
                                         Ingredient("Соус Песто", 50.0, "г")]), 1)
    sl2 = ShoppingList()
    sl2.add_recipe(Recipe("Летний салатик", [Ingredient("Огурцы", 200.0, "г"),
                                          Ingredient("Помидоры", 200.0, "г"),
                                          Ingredient("Лук репчатый", 100.0, "г")]), 1)
    sl3 = sl1 + sl2
    assert len(sl3._items) == 2

def test_add_does_not_change_ogs():
    sl1 = ShoppingList()
    sl1.add_recipe(Recipe("Пицца Песто", [Ingredient("Мука", 500.0, "г"),
                                          Ingredient("Сыр", 100.0, "г"),
                                          Ingredient("Соус Песто", 50.0, "г")]), 1)
    sl2 = ShoppingList()
    sl2.add_recipe(Recipe("Летний салатик", [Ingredient("Огурцы", 200.0, "г"),
                                             Ingredient("Помидоры", 200.0, "г"),
                                             Ingredient("Лук репчатый", 100.0, "г")]), 1)
    sl3 = sl1 + sl2
    assert len(sl1._items) == 1
    assert len(sl2._items) == 1
    assert len(sl3._items) == 2