#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
