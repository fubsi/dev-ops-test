"""Unit tests for the multiply function in math.operations module."""

from ..math.operations import multiply


def test_multiply_basic():
    """Test basic multiplication operations."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_multiply_floats():
    """Test multiplication with float numbers."""
    assert multiply(2.5, 2) == 5.0
    assert multiply(-1.5, -2) == 3.0
