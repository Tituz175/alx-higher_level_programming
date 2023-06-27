#!/usr/bin/python3
def safe_print_integer(value):
    try:
        state = isinstance(value,int)
        print("{:d}".format(value))
        return (state)
    except ValueError:
        return (state)

