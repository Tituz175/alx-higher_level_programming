#!/usr/bin/python3
"""This module contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a Square class"""
    def __init__(self, size):
        """This is the Square class constructor"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """this method calculates the area of the square"""
        return self.__size ** 2
