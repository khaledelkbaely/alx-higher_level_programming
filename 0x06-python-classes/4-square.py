#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: length of a side of the Square
        """
        self.size = size

    @property
    def size(self):
        """Getter for size attribute

        Returns:
            the current size isinstance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute

        Args:
            value: the new value for size
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Gets the area of Square

        Returns:
            the size squared
        """
        return self.__size**2
