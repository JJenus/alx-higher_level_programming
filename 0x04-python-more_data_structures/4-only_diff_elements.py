#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    n_list = [a for a in set_1 if a not in set_2]
    return n_list + [b for b in set_2 if b not in set_1]
