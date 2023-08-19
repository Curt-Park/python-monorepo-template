"""Main."""

from base import adder2


if __name__ == "__main__":
    import sys
    args = sys.argv
    assert len(args) == 3
    print(adder2.add2(int(args[1]), int(args[2])))
