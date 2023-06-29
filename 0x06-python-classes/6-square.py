#!/usr/bin/python3
"""This is a module built for Square class"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = position
        if x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(x, int) and not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """This function returns the size property"""
        return self.__size

    @property
    def position(self):
        """This function returns the position property"""
        return self.__position

    @size.setter
    def size(self, value):
        """This function set the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """This function set the position property"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if x < 1 or y < 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(x, int) and not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This function returns the area of the square"""
        return self.__size**2

    def my_print(self):
        """This function print # for the shape of a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for rows in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
