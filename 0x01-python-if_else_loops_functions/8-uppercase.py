#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        aski = ord(str[i])
        if aski <= 90:
            print("{}".format(str[i]), end='')
        else:
            print(chr(aski-32), end="")
