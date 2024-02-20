#!/usr/bin/python3
"""module for inherits_from function"""


def inherits_from(obj, a_class):
    """check if object is subclass"""
    return isinstance(obj, a_class) and type(obj) != a_class
