#!/usr/bin/python3


"""This module contains rectangle classe"""


class Rectangle:
    """This class represent a rectangle"""
    def __init__(self, width=0, height=0):
        """
        This is the rectangle class constructor

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Return:
            void
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        This method sets the width of the rectangle

        Args:
            value: the width of the rectangle to be set
        Raises:
            TypeError: if the value is not integer
            ValueError: if the value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        This method sets the height of the rectangle

        Args:
            value: the height of the rectangle to be set
        Raises:
            TypeError: if the value is not integer
            ValueError: if the value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This method calculate the area of the rectangle

        Return:
            the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method calculate the perimeter of the rectangle

        Return:
            the perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))
