#!/usr/bin/python3
"""module for pascal triangle fuction"""


def pascal_triangle(n):
    """create a list of lists represnting n
    rows of pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        tri = triangle[-1]
        row = [1]
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
