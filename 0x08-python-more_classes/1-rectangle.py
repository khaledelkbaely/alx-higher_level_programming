#!/usr/bin/pthon3
"""Module for rectangle class."""

class Rectangle:
    """Class for rectangle."""

    def __init__(self, width=0, height=0):
        """
        Instantiation wih optional width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter of width attribute

        Args:
            value: the value to set width to

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter of height attribute

        Args:
            value: the value to set height to

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
