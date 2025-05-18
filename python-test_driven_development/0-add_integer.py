#!/usr/bin/python3
"""
This module provides a function for adding two integers.

It ensures the inputs are integers or floats (which will be cast to int),
and raises a TypeError if not. The result is always an integer.

Example:
    add_integer(1, 2) returns 3
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (which are cast to integers).

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
