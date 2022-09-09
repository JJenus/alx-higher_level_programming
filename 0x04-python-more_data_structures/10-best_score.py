#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary < 1):
        return None
    score = -9999
    for k, i in a_dictionary.items():
        if i > score:
            score = i
    return score
