#!/usr/bin/python3
"""This is a Python package base file"""
import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries: A list of dictionaries to be converted.
        Returns:
            A JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"
