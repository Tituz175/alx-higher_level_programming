#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Exact same object

    Arguments:
        obj: the given object
        a_class: the class to compare against the given object
    Return:
        True if obj is same as class else False
    """

    return type(obj) == a_class
