#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "I"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCL"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCMXCVIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XLIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CDXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
