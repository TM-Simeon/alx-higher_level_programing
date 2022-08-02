#!/usr/bin/python3
"""a module to write an empty class"""


class Rectangle:
    """an empty class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
