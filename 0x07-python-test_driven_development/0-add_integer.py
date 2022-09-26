#!/usr/bin/python3
"""A function that adds two integers"""
def add_integer(a, b=98):
    """Return the integer addition of a and b

    Float arguments are type casted to ints before addition is performed.

    Raises:
        TypeError: if either a or b is a non-integer and non-float.
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer ")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer ")
    return int(a) + int(b)
