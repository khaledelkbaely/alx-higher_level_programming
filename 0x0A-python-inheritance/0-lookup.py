#!/usr/bin/python3
"""module for lookup function"""


def lookup(obj):
    """return list of available attributes and methods"""
    return list(dir(obj))
