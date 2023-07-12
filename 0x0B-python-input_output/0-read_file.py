#!/usr/bin/python3
"""Module read from a file"""


def read_file(filename="", encoding="utf-8"):
    """This function reads a file and prints it to stdout"""
    with open(filename) as f:
        print(f.read())
