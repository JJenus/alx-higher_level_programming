#!/usr/bin/python3

def uppercase(str):
    aski = ord(str)
    if aski <= 90:
        print(str)
    else:
        print(chr(aski-32))
