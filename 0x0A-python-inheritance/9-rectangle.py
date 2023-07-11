#!/usr/bin/python3
"""This module contains Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle class"""
    def __init__(self, width, height):
        """This the class constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """This method returns a string representation"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

    def area(self):
        """This method returns the area of the Rectangle"""
        return self.__width * self.__height
