"""Тестовой модуль для проверки работы функции replace_word."""
from functions.level_2.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize("test_text, test_replace_from, test_replace_to, expected",
                         [
                             ("Ходил я туда-сюда.", "я", "ты", "Ходил ты туда-сюда."),
                             ("Ходил я туда-сюда.", "", "ты", "Ходил я туда-сюда."),
                             ("Ходил я туда-сюда.", "я", "", "Ходил  туда-сюда."),
                             pytest.param("Ходил я туда-сюда.", "я", "\n", "Ходил \\n туда-сюда.",
                                          marks=pytest.mark.xfail)
                         ],
                         ids=[
                             "Normal test",
                             "Test without entering replace_from",
                             "Test without entering replace_to",
                             "Failed test because of no logic of escaping"
                         ])
def test__replace_word__testing_varios_params(test_text: str,
                                              test_replace_from: str,
                                              test_replace_to: str,
                                              expected: str) -> None:
    """Проверка функции replace_word с разными параметрами с помощью 4 тестов."""
    assert replace_word(test_text, test_replace_from, test_replace_to) == expected

@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was not given.")
def test__replace_word__test_for_not_giving_param() -> None:
    """Проверка функции replace_word на отсутствие введения одного из параметров."""
    replace_word("Ходил я туда-сюда.", "")  # type: ignore
