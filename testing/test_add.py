"""Unit tests for the add function in math.operations module."""

from ..math.operations import add

def test_add():
    """Test addition of various numbers."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5
    assert add(2.5, 3.5) == 6.0
