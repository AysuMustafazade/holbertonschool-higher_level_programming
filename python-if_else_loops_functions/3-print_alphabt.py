#!/usr/bin/python3
for i in range(97, 123):
    if i == "q" or i == "e":
        break
    print(chr(i).format(), end="")
