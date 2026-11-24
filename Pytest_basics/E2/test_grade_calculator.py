import pytest

from grade_calculator import average, has_passed, percent_to_grade


def test_percent_to_grade_normal_scores():
    assert percent_to_grade(95) == "A"
    assert percent_to_grade(85) == "B"
    assert percent_to_grade(75) == "C"
    assert percent_to_grade(65) == "D"
    assert percent_to_grade(30) == "F"


def test_percent_to_grade_lower_boundaries():
    assert percent_to_grade(90) == "A"
    assert percent_to_grade(80) == "B"
    assert percent_to_grade(70) == "C"
    assert percent_to_grade(60) == "D"


def test_percent_to_grade_just_below_boundaries():
    assert percent_to_grade(89.99) == "B"
    assert percent_to_grade(79) == "C"
    assert percent_to_grade(69) == "D"
    assert percent_to_grade(59) == "F"


def test_percent_to_grade_extremes():
    assert percent_to_grade(0) == "F"
    assert percent_to_grade(100) == "A"


def test_average():
    assert average([80, 90, 100]) == 90
    assert average([50]) == 50
    assert average([1, 2]) == 1.5


def test_has_passed_default_and_custom_pass_mark():
    assert has_passed(50) is True
    assert has_passed(49) is False
    assert has_passed(70, pass_mark=75) is False


def test_score_above_100_raises_value_error():
    with pytest.raises(ValueError):
        percent_to_grade(101)


def test_negative_score_raises_value_error_with_message():
    with pytest.raises(ValueError, match="between 0 and 100"):
        percent_to_grade(-1)


def test_text_score_raises_type_error():
    with pytest.raises(TypeError) as excinfo:
        percent_to_grade("eighty")
    assert str(excinfo.value) == "score must be a number"


def test_average_of_empty_list_raises():
    with pytest.raises(ValueError, match="no scores"):
        average([])


def test_average_rejects_a_bad_score_in_the_list():
    with pytest.raises(ValueError):
        average([80, 120])


def test_valid_score_does_not_raise():
    percent_to_grade(50)