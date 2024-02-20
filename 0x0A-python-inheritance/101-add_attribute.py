#!/usr/bin/python3
"""module for add_attribute function"""

def add_attribute(cls, att, value):
    """add new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, att, value)
