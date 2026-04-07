from datetime import datetime

from functions.level_3.three_is_subscription import \
    is_subscription
from utils import make_expense
import pytest

def test__is_subscription__subscription_true(
        expense_instance_am_10_in_netflix_at_month1,
        datetime_month_2,
        datetime_month_3
) -> None:
    history = [
        expense_instance_am_10_in_netflix_at_month1,
        make_expense(amount=10, spent_in="Netflix", spent_at=datetime_month_2),
        make_expense(amount=10, spent_in="Netflix", spent_at=datetime_month_3),
    ]

    result = is_subscription(history[-1], history)

    assert result == True


def test__is_subscription__subscription_false(expense_instance_am_10_in_netflix_at_month1) -> None:
    history = [
        expense_instance_am_10_in_netflix_at_month1,
        expense_instance_am_10_in_netflix_at_month1
    ]

    result = is_subscription(history[-1], history)

    assert result == False


@pytest.mark.xfail(raises=TypeError, reason="TypeError because params are None.")
def test__is_subscription__no_data() -> None:
    is_subscription([]) # type: ignore
