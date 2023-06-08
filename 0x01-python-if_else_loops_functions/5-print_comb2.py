#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(format(i, "02")))
    else:
        print("{}, ".format(format(i, '02')), end="")
