#!/usr/bin/python3
"""base"""
from json import dumps, loads


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        """return the JSON string of list_dictionary"""
        if list_dictionary is None or not list_dictionary:
            return '[]'
        else:
            return dumps(list_dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representaion of list_objs"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') \
                as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representaion"""
        if json_string is None or json_string == '':
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return lis of instances"""
        try:
            with open('{}.json'.format(cls.__name__), 'r', encoding='utf-8')\
                    as file:
                json_string = file.read()

                json_list = cls.from_json_string(json_string)

                return [cls.create(**dictionary) for dictionary in json_list]
        except FileNotFoundError:
            return []
