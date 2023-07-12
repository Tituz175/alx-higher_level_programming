#!/usr/bin/python3
"""Module for a simple append to a file function"""


def append_write(filename="", text=""):
    """
    this function appends a string to a text file

    Arguments:
        filename: the name of the file to append into
        text: the string to append
    Return: the number of strings written
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
