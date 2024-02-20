#!/usr/bin/python3
"""module for BaseGeometry class"""


class BaseGeometry:
    """class for geometry"""
    def area(slef):
        """computes area"""
        raise Exception("area() is not implemented")

    def integer_validator(slef, name, value):
        """validates value

        Args:
            name: variable name
            value: value of name

        Raises:
            TypeError: value is not integer
            ValueError: value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """class for rectangle"""
    def __init__(self, width, height):
        """constructor."""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
