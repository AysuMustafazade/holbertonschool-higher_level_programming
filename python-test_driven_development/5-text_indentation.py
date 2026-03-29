#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text: The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == " ":
            continue
        elif i == "." or i == "?" or i == ":":
            print("{}\n".format(text), end ="")
