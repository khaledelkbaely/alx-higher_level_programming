#!/usr/bin/python3
"""module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """return JSON representation of an object

    Args:
        filenam: file name to read obj from
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(f)
