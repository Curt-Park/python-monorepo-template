"""Tests of adder2."""

from base import adder2


def test_zero() -> None:
    """Test the neutral element."""
    assert adder2.add2(0, 0) == 0
    assert adder2.add2(0, 3) == 3
    assert adder2.add2(0, 3) == adder2.add2(3, 0)


def test_some() -> None:
    """Some unit tests of add2."""
    assert adder2.add2(1, 3) == 4
    assert adder2.add2(1, 3) == adder2.add2(3, 1)
    assert adder2.add2(100, 2) == (adder2.add2(100, 1) + adder2.add2(1, 0))
