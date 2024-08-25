
import pytest

from bun import Bun
from burger import Burger
from constants import Constants
from ingredient import Ingredient


@pytest.fixture
def ingredients():
    ingredients = []
    ingredients.append(Constants.INGREDIENTS_SAUCE)
    ingredients.append(Constants.INGREDIENTS_SAUCE2)
    ingredients.append(Constants.INGREDIENTS_SAUCE3)
    ingredients.append(Constants.INGREDIENTS_TYPE_FILLING)
    ingredients.append(Constants.INGREDIENTS_TYPE_FILLING2)
    ingredients.append(Constants.INGREDIENTS_TYPE_FILLING3)
    return ingredients

@pytest.fixture
def bun():
    bun = Bun("black bun", 20)
    return bun

@pytest.fixture
def burger_ingredients():
    ingredients_filling = []
    ingredients_filling.append(Ingredient("FILLING", "cutlet", 110))
    return ingredients_filling

@pytest.fixture
def burger():
    burger = Burger()
    return burger



