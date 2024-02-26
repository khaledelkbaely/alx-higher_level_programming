#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return the area of rectangle instance"""
        return self.width * self.height

    def display(self):
        """print rectangle to stdout"""
        s = '\n' * self.y +\
            (" " * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """return represntation for rectangle instance"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.__height)

    def __expand(self, id=None, width=None, height=None, x=None, y=None):
        """update with given parameters"""
        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """update instance"""
        if args:
            self.__expand(*args)
        elif kwargs:
            self.__expand(**kwargs)

    def to_dictionary(self):
        """return the dictionary represntation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
