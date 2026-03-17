#!/usr/bin/python3
c = input()

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False     
if True:
    print("{} is lower".format(c))
else:
    print("{} is upper".format(c))