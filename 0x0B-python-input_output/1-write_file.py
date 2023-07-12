#!/usr/bin/python3
"""Module write to a file"""


def write_file(filename="", text=""):
    """
    this function writes a string to a text file

    Arguments:
        filename: the name of the file to write into
        text: the string to write
    Return: the number of strings written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
