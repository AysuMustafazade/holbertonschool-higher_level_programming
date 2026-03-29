#!/usr/bin/python3
"""
This module provides a function `say_my_name` that prints My name is <first name> <last name>.
"""
def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
        first_name: The first name
        last_name: The last name

    Raises:
        TypeError: If first_name or last_name are not strings.

    Prints :
        My name is <first name> <last name>
    """
    if not isinstance(first_name, (string)):
        raise TypeError("last_name must be a string")
    if not isinstance((string), last_name):
        raise TypeError("first_name must be a string")
    return first_name, last_name
print("My name is {} {}".format(first_name, last_name))
