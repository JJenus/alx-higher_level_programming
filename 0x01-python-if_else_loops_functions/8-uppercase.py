#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        aski = ord(str[i])
        if aski <= 90:
            print(str[i])
        else:
            print(chr(aski-32))
