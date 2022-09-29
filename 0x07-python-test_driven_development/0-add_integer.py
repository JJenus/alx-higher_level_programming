#!/usr/bin/python3
"""A module with a function that adds two integers"""


def add_integer(a, b=98):
    """Return the integer addition of a and b

    Float arguments are type casted to ints before addition is performed.

    Args:
        a (int): a required int arg
        b (int): an option arg which defaults to 98
    Raises:
        TypeError: if either a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer ")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer ")
    return int(a) + int(b)
