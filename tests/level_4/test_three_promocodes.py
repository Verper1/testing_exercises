"""Тестовой модуль для проверки работы функции generate_promocode."""
from functions.level_4.three_promocodes import generate_promocode
import pytest


@pytest.mark.parametrize("promocode_len, expected_len",
                         [
                             (8, 8),
                             (4, 4),
                             (10, 10),
                             (1, 1),
                         ],
                         ids=[
                             "Default length",
                             "Short length",
                             "Long length",
                             "Single character"
                         ])
def test__generate_promocode__various_lengths(promocode_len, expected_len):
    """Проверка функции generate_promocode с различными длинами."""
    result = generate_promocode(promocode_len)
    assert len(result) == expected_len
    if expected_len > 0:
        assert result.isupper()
        assert result.isalpha()


def test__generate_promocode__default_length():
    """Проверка функции generate_promocode с длиной по умолчанию."""
    result = generate_promocode()
    assert len(result) == 8
    assert result.isupper()
    assert result.isalpha()


def test__generate_promocode__uniqueness():
    """Проверка уникальности генерируемых промокодов."""
    promocodes = [generate_promocode() for _ in range(100)]
    assert len(set(promocodes)) == len(promocodes)


@pytest.mark.parametrize("promocode_len",
                         [5, 6, 12],
                         ids=[
                             "Length 5",
                             "Length 6", 
                             "Length 12"
                         ])
def test__generate_promocode__character_set(promocode_len):
    """Проверка, что промокод содержит только заглавные буквы."""
    result = generate_promocode(promocode_len)
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in result)
