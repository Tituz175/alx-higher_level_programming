#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        keys = []
        for key, val in a_dictionary.items():
            if val == value:
                keys.append(key)
        for key in keys:
            del a_dictionary[key]
        return a_dictionary
