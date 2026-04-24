"""Тестовой модуль для проверки работы функции get_student_by_tg_nickname."""
from functions.level_4.two_students import Student, get_student_by_tg_nickname
import pytest


@pytest.fixture
def sample_students():
    """Фикстура с набором студентов для тестов."""
    return [
        Student("Иван", "Иванов", "@ivanov"),
        Student("Петр", "Петров", "petrov"),
        Student("Мария", "Сидорова", None),
        Student("Анна", "Козлова", "@kozlova"),
        Student("Дмитрий", "Смирнов", "smirnov"),
    ]


@pytest.mark.parametrize("telegram_username, expected_student",
                         [
                             ("ivanov", Student("Иван", "Иванов", "@ivanov")),
                             ("petrov", Student("Петр", "Петров", "petrov")),
                             ("kozlova", Student("Анна", "Козлова", "@kozlova")),
                             ("smirnov", Student("Дмитрий", "Смирнов", "smirnov")),
                             ("nonexistent", None),
                         ],
                         ids=[
                             "Username with @ in data",
                             "Username without @ in data",
                             "Another username with @",
                             "Username without @",
                             "Nonexistent username"
                         ])
def test__get_student_by_tg_nickname__various_usernames(sample_students, telegram_username, expected_student):
    """Проверка функции get_student_by_tg_nickname с различными именами пользователей."""
    result = get_student_by_tg_nickname(telegram_username, sample_students)
    assert result == expected_student


def test__get_student_by_tg_nickname__empty_list():
    """Проверка функции get_student_by_tg_nickname на пустом списке студентов."""
    result = get_student_by_tg_nickname("username", [])
    assert result is None


def test__get_student_by_tg_nickname__none_telegram_account(sample_students):
    """Проверка функции get_student_by_tg_nickname для студента без telegram."""
    result = get_student_by_tg_nickname("sidorova", sample_students)
    assert result is None


def test__get_student_by_tg_nickname__duplicate_usernames():
    """Проверка функции get_student_by_tg_nickname при дубликатах."""
    students = [
        Student("Иван", "Иванов", "ivan"),
        Student("Петр", "Петров", "ivan"),
    ]
    result = get_student_by_tg_nickname("ivan", students)
    assert result == Student("Иван", "Иванов", "ivan")


def test__get_student_by_tg_nickname__case_sensitivity():
    """Проверка функции get_student_by_tg_nickname на чувствительность к регистру."""
    students = [
        Student("Иван", "Иванов", "ivan"),
    ]
    result = get_student_by_tg_nickname("ivan", students)
    assert result == Student("Иван", "Иванов", "ivan")

    result_case = get_student_by_tg_nickname("Ivan", students)
    assert result_case is None


def test__get_student_by_tg_nickname__whitespace_handling():
    """Проверка функции get_student_by_tg_nickname на обработку пробелов."""
    students = [
        Student("Иван", "Иванов", "ivan"),
    ]
    result = get_student_by_tg_nickname("ivan", students)
    assert result == Student("Иван", "Иванов", "ivan")

    students_with_spaces = [
        Student("Петр", "Петров", "  ivan  "),
    ]
    result_spaces = get_student_by_tg_nickname("ivan", students_with_spaces)
    assert result_spaces is None
