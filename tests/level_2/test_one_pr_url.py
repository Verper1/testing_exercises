"""Тестовой модуль для проверки работы функции is_github_pull_request_url."""
from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest


@pytest.mark.parametrize("test_url, expected",
                         [
                             ("https://github.com/Verper1/typing_challenges/pull/3", True),
                             ("github.com/Verper1/typing_challenges/pull/3", False),
                             pytest.param("obman//github.com/Verper1/typing_challenges/pull/3", False, marks=pytest.mark.xfail),
                         ],
                         ids=[
                             "Normal test",
                             "Test with false url",
                             "Failed because of no checking of first index of list for https:"
                         ])
def test__is_github_pull_request_url__testing_varios_params(test_url: str,
                                              expected: bool) -> None:
    """Проверка функции is_github_pull_request_url с разными параметрами с помощью 3 тестов."""
    assert is_github_pull_request_url(test_url) == expected

@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was not given.")
def test__is_github_pull_request_url__test_for_not_giving_param() -> None:
    """Проверка функции is_github_pull_request_url на отсутствие введения одного из параметров."""
    is_github_pull_request_url()  # type: ignore


@pytest.mark.xfail(raises=AttributeError, reason="AttributeError because some params was given with another type.")
def test__is_github_pull_request_url__test_for_giving_another_type() -> None:
    """Проверка функции is_github_pull_request_url на введение аргумента в виде другого типа данных."""
    is_github_pull_request_url(123)  # type: ignore
