"""Тестовой модуль для проверки работы функции count_lines_in."""
from functions.level_4.four_lines_counter import count_lines_in
import pytest
import tempfile
import os


@pytest.fixture
def create_test_file():
    """Фикстура для создания временного файла."""
    def _create_file(content: str) -> str:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(content)
            return f.name
    return _create_file


@pytest.mark.parametrize("file_content, expected",
                         [
                             ("line1\nline2\nline3", 3),
                             ("# comment\nline1\n# another comment\nline2", 2),
                             ("   # indented comment\nline1\nline2", 2),
                             ("# only comment\n# another comment", 0),
                             ("", 0),
                             ("line1", 1),
                         ],
                         ids=[
                             "Normal test without comments",
                             "Test with comments",
                             "Test with indented comments",
                             "Only comments",
                             "Empty file",
                             "Single line"
                         ])
def test__count_lines_in__various_files(create_test_file, file_content, expected):
    """Проверка функции count_lines_in с различными содержимыми файлов."""
    file_path = create_test_file(file_content)
    try:
        assert count_lines_in(file_path) == expected
    finally:
        os.unlink(file_path)


def test__count_lines_in__nonexistent_file():
    """Проверка функции count_lines_in на несуществующем файле."""
    assert count_lines_in("nonexistent_file.txt") is None


def test__count_lines_in__directory_instead_of_file():
    """Проверка функции count_lines_in при передаче пути к директории."""
    assert count_lines_in("C:\\Users\\skuf\\PycharmProjects\\testing_exercises") is None
