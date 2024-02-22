#!/usr/bin/python3
"""module for save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """return JSON representation of an object

    Args:
        my_obj: obj to convert to json string
        filenam: file name to write obj to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
