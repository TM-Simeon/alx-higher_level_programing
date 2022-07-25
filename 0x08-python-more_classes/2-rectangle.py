#!/usr/bin/python3
"""a module to define a rectangle"""


class Rectangle:
    """ define a rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """initiate the values.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to return the area"""
        return self.idth * self.height

    def perimeter(self):
        """public method to return the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width + self.height
