#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text (str): The text to be indented
    Return:
        void
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue
        index += 1
