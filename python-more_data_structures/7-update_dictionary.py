#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    for key1 in new_dict:
        if key1 == key:
            print(f"{key1}: {value}")
    print(a_dictionary + " ---" + new_dict)
