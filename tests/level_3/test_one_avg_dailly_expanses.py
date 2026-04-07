from decimal import Decimal
from statistics import StatisticsError

from functions.level_3.one_avg_daily_expenses import \
    calculate_average_daily_expenses
from utils import make_expense
import pytest

def test__calculate_average_daily_expenses__ordinary_test(datetime_day_1, datetime_day_2, datetime_day_3) -> None:
    history = [
        make_expense(amount=100.46, spent_in="Перекрёсток", spent_at=datetime_day_1),
        make_expense(amount=102.44, spent_in="Чижик", spent_at=datetime_day_1),
        make_expense(amount=167.66, spent_in="Перекрёсток", spent_at=datetime_day_2),
        make_expense(amount=245.21, spent_in="Пятёрочка", spent_at=datetime_day_3),
    ]

    result = calculate_average_daily_expenses(history)

    assert result == Decimal('205.2566666666666666666666667')


def test__calculate_average_daily_expenses__only_one_day(datetime_day_1) -> None:
    history = [
        make_expense(amount=188.44, spent_in="Перекрёсток", spent_at=datetime_day_1),
        make_expense(amount=165.21, spent_in="Чижик", spent_at=datetime_day_1),
        make_expense(amount=222.26, spent_in="Пятёрочка", spent_at=datetime_day_1)
    ]

    result = calculate_average_daily_expenses(history)

    assert result == Decimal('575.91')


@pytest.mark.xfail(raises=StatisticsError, reason="StatisticsError because history was empty.")
def test__calculate_average_daily_expenses__no_data() -> None:
    calculate_average_daily_expenses([])
