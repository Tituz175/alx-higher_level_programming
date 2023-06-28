#!/urs/bin/python3


class Square:
    """This class represents a square"""
    def __init__(self, size=0):
        """This square class constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
