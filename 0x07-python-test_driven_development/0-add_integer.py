#!/usr/bin/python3
""" Module for add integer method."""

def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: first int
        b: second int

    Raises:
        TypeError: if a, b are not int or float

    Return:
    the sum mof the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
