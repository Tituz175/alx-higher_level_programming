#!/usr/bin/python3
"""This module contains the function is_kind_of_class(obj, a_class)"""


def is_kind_of_class(obj, a_class):
    """
    Same class or inherit from

    Arguments:
        obj: the given object
        a_class: the class to compare against the given object
    Return:
        True if obj is an instance of, or if the object is an instance
        of a class that inherited from, the specified class else False
    """

    return isinstance(obj, a_class)
