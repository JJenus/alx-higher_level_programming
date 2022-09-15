#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    nu = de = 0
    for tup in my_list:
        nu += tup[0] * tup[1]
        de += tup[1]
    return nu/de
