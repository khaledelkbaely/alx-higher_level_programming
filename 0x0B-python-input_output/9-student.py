#!/usr/bin/python3
"""module for class_to_json function"""


class Student:
    """class for Student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representaion of a Student instance"""
        return self.__dict__
