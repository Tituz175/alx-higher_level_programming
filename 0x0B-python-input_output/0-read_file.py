#!/usr/bin/python3
"""Module read from a file"""


def read_file(filename=""):
    """This function reads a file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
