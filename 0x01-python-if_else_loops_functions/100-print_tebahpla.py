#!/usr/bin/python3
number = 122
while number != 96:
    i = number
    if i % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end="")
    number -= 1
