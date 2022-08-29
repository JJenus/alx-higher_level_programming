#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth_table = []
    if len(my_list) < 1:
        return my_list
    for i in my_list:
        if i % 2 == 0:
            truth_table.append(True)
        else:
            truth_table.append(False)

    return truth_table
