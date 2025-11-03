"""Unit tests for the divide function in math.operations module."""

from ..math.operations import divide
import pytest


def test_divide_basic():
    """Test basic division operations."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5


def test_divide_negatives_and_floats():
    """Test division with negative numbers and floats."""
    assert divide(-6, 3) == -2
    assert divide(7.5, 2.5) == 3.0


def test_divide_by_zero_raises():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        divide(1, 0)
