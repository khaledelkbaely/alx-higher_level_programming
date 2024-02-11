#!/usr/bin/python3
"""
    Matrix divide module

    functions:
        matrix_divided
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix: list of lists of integers
        div: number to divide matrix elements by

    Raises:
        TypeError: if matrix is not list of lists
                    or each row of matrix is not the size
                    or div not int or float
        ZeroDivisionError: if div is 0
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    return [[round(num / div, 2) for num in row]for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
