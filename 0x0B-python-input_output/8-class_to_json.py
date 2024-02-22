#!/usr/bin/python3
"""module for class_to_json function"""


def class_to_json(obj):
    """return dictionary description with simpe data structure"""
    return obj.__dict__
