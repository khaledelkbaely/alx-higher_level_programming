#!/usr/bin/python3
"""module for to_json_string function"""
import json


def to_json_string(my_obj):
    """return JSON representation of an object

    Args:
        my_obj: obj to convert to json string
    """
    return json.dumps(my_obj)
