#!/usr/bin/python3
"""
This module contains function for arithmetic addition
"""


def add_integer(a, b=98):
    """
    This function adds two number

    Args:
        a(int or float): the first number to add
        b(int or float): the second number to add
    Return:
        integer sum of the two numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
