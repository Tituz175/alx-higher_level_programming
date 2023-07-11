#!/usr/bin/python3
"""This module contains the function inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """
    Only sub class of

    Arguments:
        obj: the given object
        a_class: the class to compare against the given object
    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class else False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
