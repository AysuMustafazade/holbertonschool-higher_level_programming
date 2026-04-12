#!/usr/bin/python3
"""inherits from the secified class"""


def inherits_from(obj, a_class):
    """inherits from the secified class"""
    if type(obj) is a_class:
        return isinstance(obj, a_class)
