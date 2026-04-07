from datetime import datetime

import pytest

from tests.level_3.utils import make_expense


@pytest.fixture
def datetime_day_1():
    return datetime(2025, 1, 1, 10, 0)

@pytest.fixture
def datetime_day_2():
    return datetime(2025, 1, 2, 10, 0)

@pytest.fixture
def datetime_day_3():
    return datetime(2025, 1, 3, 10, 0)

@pytest.fixture
def datetime_month_1():
    return datetime(2025, 1, 1)

@pytest.fixture
def datetime_month_2():
    return datetime(2025, 2, 1)

@pytest.fixture
def datetime_month_3():
    return datetime(2025, 3, 1)

@pytest.fixture
def expense_instance_am_10_in_netflix_at_month1(datetime_month_1):
    return make_expense(amount=10, spent_in="Netflix", spent_at=datetime_month_1)