#!/usr/bin/python3
'''module with class Rectangle'''
Rectangle = __import__('8-rectangle').Rectangle


class Rectangle(Rectangle):
    '''Rectangle class'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines an area."""
        area = self.__height*self.__width
        return area

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
