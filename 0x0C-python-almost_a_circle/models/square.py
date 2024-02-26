#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """class contructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string info for Square instance"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __expand(self, id=None, size=None, x=None, y=None):
        """update with given parameters"""
        if id:
            self.id = id
        if size:
            self.size = size
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
        """return the dictionary represntation of a Square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
