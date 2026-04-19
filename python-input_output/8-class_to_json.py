#!/usr/bin/python3
"""Converting a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description of object for JSON serialization."""
    return obj.__dict__
