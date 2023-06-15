#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = max(a_dictionary.values())
        for k,v in a_dictionary.items():
            if v == best_score:
                return k
    else:
        return None
