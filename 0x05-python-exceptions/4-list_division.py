#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for num in range(list_length):
        result = 0
        try:
            result = my_list_1[num]/my_list_2[num]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return (result_list)
