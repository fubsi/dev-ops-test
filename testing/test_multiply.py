from math.operations import multiply


def test_multiply_basic():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_multiply_floats():
    assert multiply(2.5, 2) == 5.0
    assert multiply(-1.5, -2) == 3.0
