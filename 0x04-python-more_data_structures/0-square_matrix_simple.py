#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    for submat in matrix:
        ret.append(list(map(lambda x: x ** 2, submat)))
    return ret
