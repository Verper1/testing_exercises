"""Тестовой модуль для проверки работы функции first."""
from functions.level_2.three_first import first
import pytest


@pytest.mark.parametrize("test_items, test_default, expected",
                         [
                             ([1, 2, 3], None, 1),
                             pytest.param([], "some str", pytest.raises(TypeError), marks=pytest.mark.xfail),
                             ([], 21, 21),
                             pytest.param(["1", "2"], None, pytest.raises(TypeError), marks=pytest.mark.xfail)
                         ],
                         ids=[
                             "Normal test",
                             "Failed because of func must return None or int type. def first(...) -> int | None",
                             "Test for returning default if list is empty",
                             "Failed because of vars in items expected to be int. items: list[int]"
                         ])
def test__first__testing_varios_params(test_items: list[int],
                                       test_default: int | None | str,
                                       expected: int | None) -> None:
    """Проверка функции first с разными параметрами с помощью 4 тестов."""
    assert first(test_items, test_default) == expected

@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was not given.")
def test__first__test_for_not_giving_param() -> None:
    """Проверка функции first на отсутствие введения одного из параметров."""
    first()  # type: ignore


@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was given with another type.")
def test__first__test_for_giving_another_type() -> None:
    """Проверка функции first на введение аргумента в виде другого типа данных."""
    first(123)  # type: ignore
