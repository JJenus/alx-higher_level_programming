#!/usr/bin/python3

def best_score(a_dictionary):
    score = -9999
    for k, i in a_dictionary.items():
        if i > score:
            score = i
    return score