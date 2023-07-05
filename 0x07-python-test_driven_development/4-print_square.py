#!/usr/bin/python3
"""
This is module contain a function that prints a square with the character #
"""


def print_square(size):
    """
    This prints a square with the character # depending on the given size

    Args:
        size (int): size of the square
    Return:
        void
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for num in range(size):
        print("#" * size)
