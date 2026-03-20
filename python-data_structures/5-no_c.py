#!/usr/bin/python3

def no_c(my_string):
    char1 = "c"
    char2 = "C"
    new_string = ''.join(char for char in my_string if char != char1 or char != char2)

return my_string
