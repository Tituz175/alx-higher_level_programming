#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
last = sign * int(str(number)[-1])
if last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
else:
    print(f"Last digit of {number} is {last} and is 0")
