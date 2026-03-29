#!/usr/bin/python3
"""
This module provides one function, add_integer(a, b).
The function adds two integers and handles type validation.
"""

def add_integer(a, b=98):
    """Adds two integers.
    Returns an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
