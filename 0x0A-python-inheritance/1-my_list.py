#!/usr/bin/python3
"""module for MyList class"""


class MyList(list):
    def print_sorted(self):
        copy = self[:]
        copy.sort()
        print(copy)
