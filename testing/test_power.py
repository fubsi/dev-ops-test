"""Unit tests for the power function in math.operations module."""

from math.operations import power


def test_power_basic():
    """Test basic power operations."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_power_negatives_and_floats():
    """Test power with negative exponents and floats."""
    assert power(2, -1) == 0.5
    assert power(4.5, 2) == 20.25
