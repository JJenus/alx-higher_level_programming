#!/usr/bin/python3

def best_score(a_dictionary):
    score = -9999
    key = None
    for k, i in a_dictionary.items():
        if i > score:
            score = i
            key = k
    return key
