#!/usr/bin/python3
"""Module for rectangle class."""


class Rectangle:
    """Class for rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantiation wih optional width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        computes the are of rectangle

        Return:
            the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        computes the perimeter of rectangle

        Return:
            the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        make rectangle with '#'

        Return:
            rectangle with '#' or empty string width or height is zero
        """
        s = ''
        if self.__width == 0 or self.__height == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += '{}'.format(self.print_symbol)
            if i != self.__height - 1:
                s += '\n'
        return s

    def __repr__(self):
        """
        return string representaion of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        print a message on deletion of instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare two rectangles based on area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle

        Return:
            the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
