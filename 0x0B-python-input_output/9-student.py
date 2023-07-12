#!/usr/bin/python3
"""This is a python module for a Student class"""


class Student:
    """This is a class representation of a Student"""
    def __init__(self, first_name, last_name, age):
        """The student class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
