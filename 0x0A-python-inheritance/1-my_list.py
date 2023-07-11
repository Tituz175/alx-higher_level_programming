#!/usr/bin/python3
"""This module contains mylist class drived from the python list object"""


class MyList(list):
    """The my list class"""
    def __init__(self):
        """The constructor for mylist"""
        list.__init__(self)

    def print_sorted(self):
        """this method prints the sorted list"""
        print(sorted(self))
