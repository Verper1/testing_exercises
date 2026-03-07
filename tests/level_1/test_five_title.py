from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize("test_input_1, test_input_2, expected",
                         [
                             ("Русские истории", 100, "Copy of Русские истории"),
                             ("Copy of Русские истории", 100, "Copy of Русские истории (2)"),
                             ("Copy of Русские истории (2)", 100, "Copy of Русские истории (3)"),
                             ("Copy of Русские истории (3)", 35, "Copy of Русские истории (3)")
                         ], ids=["Normal test", "Adding (2)", "Adding (3)", "Length param"])
def test_change_copy_item(test_input_1, test_input_2, expected):
    assert change_copy_item(test_input_1, test_input_2) == expected