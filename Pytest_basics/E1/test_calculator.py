import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_floats_uses_approx():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_gives_negative_result():
    assert subtract(3, 5) == -2


class TestMultiply:
    def test_multiply(self):
        assert multiply(4, 3) == 12

    def test_multiply_by_zero(self):
        assert multiply(7, 0) == 0


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_always_returns_a_float():
    assert isinstance(divide(10, 5), float)