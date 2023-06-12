#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a:
        if len(tuple_a) > 1:
            a1, a2 = tuple_a
        else:
            a1 = tuple_a[0]
            a2 = 0
    else:
        a1 = 0
        a2 = 0

    if tuple_b:
        if len(tuple_b) > 1:
            b1, b2 = tuple_b
        else:
            b1 = tuple_b[0]
            b2 = 0
    else:
        b1 = 0
        b2 = 0

    return (a1 + b1, a2 + b2)
