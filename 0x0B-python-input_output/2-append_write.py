#!/usr/bin/python3
"""module for append_write function"""


def append_write(filename='', text=''):
    """write file and print to stdout

    Args:
        filename: file name to write
        text: text to write to filename
    """
    with open(filename, 'a', 'utf-8') as file:
        file.write(text)
