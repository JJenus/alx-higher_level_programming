#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) < 1:
        return None
    score = -999999
    key = None
    for k, i in a_dictionary.items():
        if i > score:
            score = i
            key = k
    return key
