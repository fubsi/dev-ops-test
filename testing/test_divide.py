import pytest
from math.operations import divide


def test_divide_basic():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5


def test_divide_negatives_and_floats():
    assert divide(-6, 3) == -2
    assert divide(7.5, 2.5) == 3.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)
