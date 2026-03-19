#!/usr/bin/python3

def no_c(my_string):
    a=list(my_string)
    for x in a:
        if x=="c" or x == "C":
             x==""
    "".join(a)    
