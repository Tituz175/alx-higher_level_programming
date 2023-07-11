#!/usr/bin/python3
"""This module contains BaseGeometry class"""


class BaseGeometry:
    """The base class for Geometry"""
    def area(self):
        """This function returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the integer value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
