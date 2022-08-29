#!/usr/bin/python3

func = __import__('2-replace_in_list').replace_in_list

alist = [12, 44, 55, 88, 11]
el = 'racist'
in1 = 2
in2 = -3
in3 = 23
print(f"index: {in1} new element: {el}\n prev list: {alist} \n new list:{func(alist, in1, el)}\n")
print(f"index: {in2} new element: {el}\n prev list: {alist} \n new list:{func(alist, in2, el)}\n")
print(f"index: {in3} new element: {el}\n prev list: {alist} \n new list:{func(alist, in3, el)}\n")
