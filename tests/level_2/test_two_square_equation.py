"""Тестовой модуль для проверки работы функции solve_square_equation."""
from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
    "test_square_coefficient, test_linear_coefficient, test_const_coefficient, expected",
    [
        (1.0, -3.0, 2.0, (1.0, 2.0)),
        (1.0, 2.0, 1.0, (-1.0, -1.0)),
        (1.0, 1.0, 1.0, (None, None)),
        (0.0, 2.0, 4.0, (-2.0, None)),
        (0.0, 0.0, 5.0, (None, None)),
        (1.0, 0.0, -4.0, (-2.0, 2.0)),
        pytest.param("1", "2", "3", pytest.raises(TypeError),
                     marks=pytest.mark.xfail),
    ],
    ids=[
        "Normal test",
        "Quadratic equation with one root (D = 0)",
        "Quadratic equation with negative discriminant",
        "Linear equation because a = 0",
        "Degenerate equation (a = 0 and b = 0)",
        "Two symmetric roots",
        "Failed because coefficients must be float",
    ],
)
def test__solve_square_equation__testing_varios_params(
    test_square_coefficient: float,
    test_linear_coefficient: float,
    test_const_coefficient: float,
    expected: tuple[float | None, float | None],
) -> None:
    """Проверка функции solve_square_equation с разными параметрами."""
    assert solve_square_equation(
        test_square_coefficient,
        test_linear_coefficient,
        test_const_coefficient
    ) == expected


@pytest.mark.xfail(raises=TypeError, reason="TypeError because some params were not given.")
def test__solve_square_equation__test_for_not_giving_param() -> None:
    """Проверка функции solve_square_equation на отсутствие введения параметров."""
    solve_square_equation()  # type: ignore
