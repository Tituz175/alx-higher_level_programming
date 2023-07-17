#!/usr/bin/python3
"""This is a Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square and inherits
    its properties from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This function returns a string representation of the Square class
        """
        return (
            f"[{Square.__name__}]\
 ({self.id}) {self.x}/{self.y} - {self.width}"
        )
