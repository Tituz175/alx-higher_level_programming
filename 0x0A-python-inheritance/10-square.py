#!/usr/bin/python3
"""This module contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a Square class"""
    def __init__(self, size):
        """This is the Square class constructor"""
        super().__init__(size, size)

    def __str__(self):
        return super().__str__()
