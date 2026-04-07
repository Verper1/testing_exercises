from enum import Enum

from functions.level_3.models import ExpenseCategory, Expense

from functions.level_3.two_expense_categorizer import \
    guess_expense_category
from utils import make_expense
import pytest


@pytest.mark.parametrize(
    "test_expense, expected",
    [
        (make_expense(spent_in="APPLE.COM/BILL 12345"), ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        (make_expense(spent_in="BOLT.EU*TRIP 438"), None),
        (make_expense(spent_in="ASADOR - Yerevan"), ExpenseCategory.BAR_RESTAURANT),
        (make_expense(spent_in="PHARMACY CITY CENTER"), None),
        pytest.param(make_expense(), pytest.raises(TypeError),
                     marks=pytest.mark.xfail)
    ],
    ids=[
        "Online subscriptions",
        "None because of *",
        "Bar restaurant",
        "Pharmacy but not pharm. None",
        "TypeError because nothing was given"
    ]
)
def test__guess_expense_category__varios_params(test_expense: Expense, expected: Enum):
    assert guess_expense_category(test_expense) == expected
