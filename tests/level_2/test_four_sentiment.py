"""Тестовой модуль для проверки работы функции check_tweet_sentiment."""
from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest
from utils import str_for_one_test,good_words, bad_words


@pytest.mark.parametrize("test_text, test_good_words, test_bad_words, expected",
                         [
                             ("Я ненавижу это!", good_words, bad_words, "BAD"),
                             ("Я люблю это!", good_words, bad_words, "GOOD"),
                             ("Я долго думал об этом.", good_words, bad_words, None),
                             pytest.param(str_for_one_test, good_words, bad_words, "BAD", marks=pytest.mark.xfail),
                         ],
                         ids=[
                             "Test with bad word",
                             "Test with good word",
                             "Test without good and bad words",
                             "Failed test because of too many good words that was used in bad way"
                         ])
def test__check_tweet_sentiment__testing_varios_params(test_text: str,
                                              test_good_words: set[str],
                                              test_bad_words: set[str],
                                              expected: str | None) -> None:
    """Проверка функции check_tweet_sentiment с разными параметрами с помощью 4 тестов."""
    assert check_tweet_sentiment(test_text, test_good_words, test_bad_words) == expected

@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was not given.")
def test__check_tweet_sentiment__test_for_not_giving_param() -> None:
    """Проверка функции check_tweet_sentiment на отсутствие введения одного из параметров."""
    check_tweet_sentiment("Я люблю это!")  # type: ignore


@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params was given with another type.")
def test__check_tweet_sentiment__test_for_giving_another_type() -> None:
    """Проверка функции check_tweet_sentiment на введение нескольких аргументов в виде другого типа данных."""
    check_tweet_sentiment("Я люблю это!", "123", 123)  # type: ignore
