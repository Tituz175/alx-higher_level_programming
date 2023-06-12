#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]
        for num in range(1, len(my_list)):
            if my_list[num] > max_value:
                max_value = my_list[num]
        return max_value
    else:
        return None
