#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_obj = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    number = 0
    for string in roman_string:
        if string == "I" and (
                roman_string[roman_string.index(string) + 1] == "X"
                or roman_string[roman_string.index(string) + 1] == "V"
                ):
            number -= roman_obj[string]
        else:
            number += roman_obj[string]
    return number
