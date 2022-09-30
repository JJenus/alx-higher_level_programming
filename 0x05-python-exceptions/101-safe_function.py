#!/usr/bin/python3

def add(a, b):
    print(a+b)

def safe_function(fct, *args):
    fct(args)


safe_function(add, 10, 5)
