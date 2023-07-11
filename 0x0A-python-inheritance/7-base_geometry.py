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
            message = f"{name} must be an integer"
            raise TypeError(message)

        if value < 1:
            message = f"{name} must be greater than 0"
            raise ValueError(message)
