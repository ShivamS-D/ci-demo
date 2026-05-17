import pytest
from src.calculator import add, subtract, multiply, divide


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5


def test_subtract_normal():
    assert subtract(10, 4) == 6


def test_subtract_resulting_in_negative():
    assert subtract(3, 10) == -7


def test_multiply_normal():
    assert multiply(4, 3) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
