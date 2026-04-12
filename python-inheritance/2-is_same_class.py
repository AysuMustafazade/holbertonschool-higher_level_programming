#!/usr/bin/python3
"""if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
