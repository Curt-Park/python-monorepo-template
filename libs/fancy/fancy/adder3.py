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


if __name__ == "__main__":
    import sys
    args = sys.argv
    assert len(args) == 4
    print(add3(int(args[1]), int(args[2]), int(args[3])))
