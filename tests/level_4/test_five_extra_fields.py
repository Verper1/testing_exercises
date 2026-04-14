"""Тестовой модуль для проверки работы функций с конфигурационными файлами."""
from functions.level_4.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field
import pytest
import tempfile
import os


@pytest.fixture
def create_test_config():
    """Фикстура для создания временного конфигурационного файла."""
    def _create_config(content: str) -> str:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.cfg', delete=False, encoding='utf-8') as f:
            f.write(content)
            return f.name
    return _create_config


@pytest.mark.parametrize("config_content, field_name, expected",
                         [
                             ("[tool:app-config]\nextra_fields = name: str", "extra_fields", "name: str"),
                             ("[tool:app-config]\nother_field = value", "extra_fields", None),
                             ("[tool:app-config]\n", "extra_fields", None),
                             ("[other-section]\nextra_fields = value", "extra_fields", None),
                         ],
                         ids=[
                             "Normal test with extra_fields",
                             "Missing extra_fields field",
                             "Empty section",
                             "Wrong section"
                         ])
def test__fetch_app_config_field__various_configs(create_test_config, config_content, field_name, expected):
    """Проверка функции fetch_app_config_field с различными конфигурациями."""
    config_path = create_test_config(config_content)
    try:
        assert fetch_app_config_field(config_path, field_name) == expected
    finally:
        os.unlink(config_path)


@pytest.mark.parametrize("config_content, expected",
                         [
                             ("[tool:app-config]\nextra_fields = name: str", {"name": str}),
                             ("[tool:app-config]\nextra_fields = ", {}),
                             ("[tool:app-config]\n", {}),
                             ("[tool:app-config]\nextra_fields = name: str", {"name": str}),
                         ],
                         ids=[
                             "Normal test with single field",
                             "Empty extra_fields",
                             "No extra_fields section",
                             "Single field test"
                         ])
def test__fetch_extra_fields_configuration__various_configs(create_test_config, config_content, expected):
    """Проверка функции fetch_extra_fields_configuration с различными конфигурациями."""
    config_path = create_test_config(config_content)
    try:
        result = fetch_extra_fields_configuration(config_path)
        assert result == expected
    finally:
        os.unlink(config_path)


def test__fetch_extra_fields_configuration__nonexistent_file():
    """Проверка функции fetch_extra_fields_configuration на несуществующем файле."""
    result = fetch_extra_fields_configuration("nonexistent_file.cfg")
    assert result == {}


def test__fetch_app_config_field__nonexistent_file():
    """Проверка функции fetch_app_config_field на несуществующем файле."""
    result = fetch_app_config_field("nonexistent_file.cfg", "extra_fields")
    assert result is None
