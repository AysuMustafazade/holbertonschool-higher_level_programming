#!/usr/bin/python3

def delete_by_key(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
