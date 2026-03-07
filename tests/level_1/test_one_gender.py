from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",
                         [
                             ("Пошёл", "Пошла", "male", "Пошёл"),
                             ("Читал", "Читала", "female", "Читала")
                         ], ids=["Male response", "Female response"])
def test_genderalize(test_input_1, test_input_2, test_input_3, expected):
    assert genderalize(test_input_1, test_input_2, test_input_3) == expected
