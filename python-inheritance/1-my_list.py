#!/usr/bin/python3
""" a class that inherits from list"""

class MyList(list):
    """ a class that inherits from list"""
    def print_sorted(self):
        """ prints the list, but sorted"""
        print(self.sorted())
