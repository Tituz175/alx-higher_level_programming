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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            cls: The class of the objects.
            list_objs: A list of objects to be saved.
        """
        my_Objlist = [obj.to_dictionary() for obj in list_objs]
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as f:
            if my_Objlist:
                f.write(cls.to_json_string(my_Objlist))
            else:
                f.write("[]")
