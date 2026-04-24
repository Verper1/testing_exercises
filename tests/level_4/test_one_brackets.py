"""Тестовой модуль для проверки работы функции delete_remove_brackets_quotes."""
from functions.level_4.one_brackets import delete_remove_brackets_quotes
import pytest


@pytest.mark.parametrize("test_input, expected",
                         [
                             ("{test}", "es"),
                             ("{hello world}", "ello worl"),
                             ("normal_string", "normal_string"),
                             ("{ab}", ""),
                             ("{abc}", "b"),
                             ("{abcd}", "bc"),
                         ],
                         ids=[
                             "Normal test with brackets",
                             "Test with spaces",
                             "Test without brackets",
                             "Two characters inside",
                             "Three characters inside",
                             "Four characters inside"
                         ])
def test__delete_remove_brackets_quotes__various_strings(test_input, expected):
    """Проверка функции delete_remove_brackets_quotes с различными строками."""
    assert delete_remove_brackets_quotes(test_input) == expected


@pytest.mark.xfail(raises=IndexError, reason="String is too short")
def test__delete_remove_brackets_quotes__empty_string():
    """Проверка функции delete_remove_brackets_quotes на пустой строке."""
    delete_remove_brackets_quotes("")


def test__delete_remove_brackets_quotes__single_char():
    """Проверка функции delete_remove_brackets_quotes на строке из одного символа."""
    result = delete_remove_brackets_quotes("{")
    assert result == ""


def test__delete_remove_brackets_quotes__edge_cases():
    """Проверка функции delete_remove_brackets_quotes на граничных случаях."""
    assert delete_remove_brackets_quotes("{") == ""

    assert delete_remove_brackets_quotes("test{") == "test{"
    assert delete_remove_brackets_quotes("}test") == "}test"
