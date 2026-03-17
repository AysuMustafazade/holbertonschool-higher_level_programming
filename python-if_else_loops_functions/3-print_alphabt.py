#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == "q" or chr(i) == "e":
        break
    print(chr(i).format(), end="")
