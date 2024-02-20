#!/usr/bin/python3
"""module for is_same_class function"""


def is_same_class(obj, a_class):
    """return true if obj is exactly an instance of the class"""
    return type(obj) is a_class
