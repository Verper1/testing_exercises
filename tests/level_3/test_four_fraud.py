import decimal
import datetime

from functions.level_3.four_fraud import find_fraud_expenses
from utils import make_expense


def test__find_fraud_expenses__fraud_detected_three_identical_transactions(datetime_day_1):
    history = [
        *[make_expense(1500, "Shop A", datetime_day_1) for _ in range(3)]
    ]

    result = find_fraud_expenses(history)

    assert len(result) == 3
    assert all(e.amount == decimal.Decimal("1500") for e in result)
    assert all(e.spent_in == "Shop A" for e in result)


def test__find_fraud_expenses__no_fraud_only_two_transactions(datetime_day_1):
    history = [
        *[make_expense(2000, "Cafe", datetime_day_1) for _ in range(2)]
    ]

    result = find_fraud_expenses(history)

    assert result == []


def test__find_fraud_expenses__no_fraud_different_times_count_separately():
    history = [
        make_expense(1500, "Shop A", datetime.datetime(2025, 1, 1, 10, 0)),
        make_expense(1500, "Shop A", datetime.datetime(2025, 1, 1, 11, 0)),
        make_expense(1500, "Shop A", datetime.datetime(2025, 1, 1, 12, 0)),
    ]

    result = find_fraud_expenses(history)

    assert result == []


def test__find_fraud_expenses__no_fraud_amount_over_limit(datetime_day_1):
    history = [
        *[make_expense(6000, "Shop A", datetime_day_1) for _ in range(3)]
    ]

    result = find_fraud_expenses(history)

    assert result == []


def test__find_fraud_expenses__two_separate_fraud_groups_detected(datetime_day_1, datetime_day_2):
    history = [
        *[make_expense(1000, "Shop A", datetime_day_1) for _ in range(3)],

        *[make_expense(3000, "Website B", datetime_day_2) for _ in range(3)],
    ]

    result = find_fraud_expenses(history)

    assert len(result) == 6

    assert sum(e.amount == decimal.Decimal("1000") for e in result) == 3
    assert sum(e.amount == decimal.Decimal("3000") for e in result) == 3