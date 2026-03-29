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

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            if i < len(text):
                print("\n")
            continue
        print(text[i], end="")
        i += 1
