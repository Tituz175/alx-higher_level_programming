#!/usr/bin/python3
"""This is a Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a rectangle and inherits
    its properties from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        This function returns a string representation of the Rectangle class
        """
        return (
            f"[Rectangle]\
 ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        )

    @property
    def width(self):
        """This gives the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This gives the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This gives the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the x of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This gives the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the y of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Returns the stdout instance of the rectangle with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()
