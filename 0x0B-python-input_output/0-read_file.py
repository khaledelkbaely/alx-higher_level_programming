#!/usr/bin/python3
"""module for read_file function"""


def read_file(filename=''):
    """read file and print to stdout

    Args:
        filename: file name to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
