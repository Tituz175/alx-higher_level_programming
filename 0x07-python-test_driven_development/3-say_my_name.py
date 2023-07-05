#!/usr/bin/python3
"""
This is a module that contains a function that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    This is a function that prints a sentence wiht the given names

    Args:
        first_name: string
        last_name: string
    Return:
        void
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
