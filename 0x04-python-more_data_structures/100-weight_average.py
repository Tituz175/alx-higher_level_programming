#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight = 0
        ave = 0
        for num in my_list:
            weight += (num[0] * num[1])
            ave += num[1]
        return weight / ave
    else:
        return 0
