#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size: length of a side of the Square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position attribute

        Returns:
            the current position instance attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute

        Args:
            value: the new value for position
        """
        if (not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Gets the area of Square

        Returns:
            the size squared
        """
        return self.__size**2

    def my_print(self):
        """print to stdout square."""
        if self.__size == 0:
            print()
            return
        print('\n' * self.__position[1], end='')
        for i in range(0, self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.size)
