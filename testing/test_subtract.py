"""Unit tests for the subtract function in math.operations module."""

from ..math.operations import subtract


def test_subtract_basic():
    """Test basic subtraction operations."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


def test_subtract_negatives_and_floats():
    """Test subtraction with negative numbers and floats."""
    assert subtract(-2, 3) == -5
    assert subtract(2.5, 1.0) == 1.5
