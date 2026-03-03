from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",
                         [
                             ("LPA", "LPA12", None, "LPA/LPA12"),
                             ("LPA", "LPA12", {"is_student": "true"}, "LPA/LPA12?is_student=true"),
                             ("LPA", "LPA12", {"is_student": "true", "track": "Django"},
                              "LPA/LPA12?is_student=true&track=Django"),
                             ("LPA", "LPA12", {"is_student": "true", "track": "Django", "is_homework_done": "no"},
                              "LPA/LPA12?is_student=true&track=Django&is_homework_done=no"),
                             ("", "", None, "/")
                         ], ids=["Normal test", "Test with 1 param", "Test with 2 param", "Test with 3 param",
                                 "Noting in params"])
def test_build_url(test_input_1, test_input_2, test_input_3, expected):
    assert build_url(test_input_1, test_input_2, test_input_3) == expected