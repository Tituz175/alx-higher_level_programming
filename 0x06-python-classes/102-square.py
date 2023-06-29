#!/usr/bin/python3
"""This is a module built for Square class"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    @property
    def size(self):
        """This function returns the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function returns the set the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns the area of the square"""
        return self.__size**2
