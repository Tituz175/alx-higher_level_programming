#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        my_set = {i for i in my_list}
        total = 0
        for num in my_set:
            total += num
        return total
