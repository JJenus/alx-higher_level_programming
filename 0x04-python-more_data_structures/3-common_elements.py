#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = [i for i in set(set_1) if i in set_2]
    return list(set(set_3 + [i for i in set(set_2) if i in set_1]))
