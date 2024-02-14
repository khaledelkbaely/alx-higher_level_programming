#!/usr/bin/python3
"""Module for print square function"""


def print_square(size):
    """print square with size

    Args:
        size: size of the side length of square

    Raises:
        TypeError: if size is not integer or size is float less than zero
        ValueError: if size is less than zero
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt')
