#!/usr/bin/python3
'''module with class Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Defines an area."""
        area = self.__size**2
        return area

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
