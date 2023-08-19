"""Example module of the fancy library"""

from base.adder2 import add2


def add3(x: int, y: int, z: int) -> int:
    """Add three integers.

    Args:
        x: the 1st operand
        y: the 2nd operand
        z: the 3rd operand
    Returns:
        The sum of x, y, and z
    """
    return add2(add2(x, y), z)
