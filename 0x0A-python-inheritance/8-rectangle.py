#!/usr/bin/python3
"""a module to write an empty class"""


class Rectangle:
    """an empty class"""
    def __init__(self, width, height):
        """the init method for the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method for the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method for the class"""
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
