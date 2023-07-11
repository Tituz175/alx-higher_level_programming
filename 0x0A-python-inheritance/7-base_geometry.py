#!/usr/bin/python3
"""This module contains BaseGeometry class"""


class BaseGeometry:
    """The base class for Geometry"""
    def area(self):
        """This function returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the integer value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
