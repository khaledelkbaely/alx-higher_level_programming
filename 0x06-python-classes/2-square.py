#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: length of a side of the Square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
