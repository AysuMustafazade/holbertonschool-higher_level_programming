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

    for i in range(len(text)):
        if i == 0 and text[i] == ' ':
            continue

        if i > 0 and text[i] == ' ' and text[i - 1] in ".?: ":
            continue

        print(text[i], end="")

        if text[i] in ".?:":
            print("\n", end="")
            print("")
