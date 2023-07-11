#!/usr/bin/python3
"""This module contains a function"""


def add_attribute(obj, name, value):
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
        