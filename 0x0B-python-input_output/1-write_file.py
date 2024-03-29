#!/usr/bin/python3
"""module for write_file function"""


def write_file(filename='', text=''):
    """write file and print to stdout

    Args:
        filename: file name to write
        text: text to write to filename
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
