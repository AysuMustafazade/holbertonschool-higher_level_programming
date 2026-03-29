#!/usr/bin/python3
"""Module for adding integers.
Contains one function: add_integer(a, b).
"""


def add_integer(a, b=98):
    """Adds two integers or floats (casted to integers).

    Args:
        a: The first number.
        b: The second number, defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        The integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    