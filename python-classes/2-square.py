#!/usr/bin/python3
"""This module defines a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.__size = size
    if not isinstance (__size, int):
        raise TypeError("size must be an integer")
    if __size < 0:
        raise ValueError("size must be >= 0")
