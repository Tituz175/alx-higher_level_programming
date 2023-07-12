#!/usr/bin/python3
"""This is a python module for a Student class"""


class Student:
    """This is a class representation of a Student"""

    def __init__(self, first_name, last_name, age):
        """The student class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if self.__dict__.get(item):
                    new_dict[item] = self.__dict__.get(item)
            return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        """
        self.__init__(
            json.get("first_name"), json.get("last_name"), json.get("age")
        )
