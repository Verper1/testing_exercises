import datetime

from functions.level_1.two_date_parser import compose_datetime_from
import pytest


@pytest.mark.parametrize("test_input_1, test_input_2, expected",
                         [
                             ("today", "14:30", datetime.datetime(2026, 3, 3, 14, 30)),
                             ("tomorrow", "09:15", datetime.datetime(2026, 3, 4, 9, 15)),
                             pytest.param("tomorroww", "09:15",
                                          datetime.datetime(2026, 3, 4, 9, 15),
                                          marks=pytest.mark.xfail)
                         ], ids=["Test today", "Test tomorrow", "AssertionError because tomorroww"])
def test_compose_datetime_from(test_input_1, test_input_2, expected):
    assert compose_datetime_from(test_input_1, test_input_2) == expected

@pytest.mark.xfail(raises=ValueError, reason="ValueError because params are None")
def test_compose_datetime_from_2():
    compose_datetime_from("", "")