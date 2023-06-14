#!/usr/bin/python3
import ctypes

l = ["Hello", "World"]

c_lib = ctypes.CDLL("./c_lib.so")
c_lib.print_list.argtypes = [ctypes.py_object]
c_lib.print_list(l)
del l[1]
c_lib.print_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
c_lib.print_list(l)
l = []
c_lib.print_list(l)
l.append(0)
c_lib.print_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
c_lib.print_list(l)
l.pop()
c_lib.print_list(l)
