"""Main."""

from fancy import adder3


if __name__ == "__main__":
    import sys
    args = sys.argv
    assert len(args) == 4
    print(adder3.add3(int(args[1]), int(args[2]), int(args[3])))
