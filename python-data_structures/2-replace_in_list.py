#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list)-1):
        return my_list
    else:
        return s.replace(my_list[idx], element) for s in my_list
