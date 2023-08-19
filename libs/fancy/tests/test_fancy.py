"""Tests of adder3."""

from libs.fancy.fancy import adder3


def test_zero() -> None:
    """Test of add3 with zero"""
    assert adder3.add3(0, 0, 0) == 0
    assert adder3.add3(0, 1, 0) == 1
    assert adder3.add3(0, 1, 2) == 3
    assert adder3.add3(1, 2, 0) == 3


def test_some() -> None:
    """Some unit tests of add3."""
    assert adder3.add3(1, 2, 3) == 6
    assert adder3.add3(1, 2, 3) == adder3.add3(3, 2, 1)
    assert adder3.add3(100, 2, 3) == 105
