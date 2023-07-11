#!/usr/bin/python3
"""This module contains a class"""


class MyInt(int):
    """My integer class"""
    def __eq__(self, other):
        """this method returns false if other is equal self.real"""
        return False

    def __ne__(self, other):
        """this method returns true if other is not equal self.real"""
        return True
