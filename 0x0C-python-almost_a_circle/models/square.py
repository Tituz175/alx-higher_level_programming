#!/usr/bin/python3
"""This is a Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square and inherits
    its properties from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This function returns a string representation of the Square class
        """
        return (
            f"[{Square.__name__}]\
 ({self.id}) {self.x}/{self.y} - {self.size}"
        )

    @property
    def size(self):
        """This gives the size of the rectangle"""
        return self.__width

    @size.setter
    def size(self, value):
        """This sets the size of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable-length argument list
            containing the new values for the attributes.
            The arguments should be provided in
            the order: id, size, x, y.
        """

        if args:
            attributes = ["id", "size", "x", "y"]
            for key, value in zip(attributes, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
