#!/usr/bin/python3
"""module for MyList class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """function to print sorted list without changing original"""
        copy = self[:]
        copy.sort()
        print(copy)
