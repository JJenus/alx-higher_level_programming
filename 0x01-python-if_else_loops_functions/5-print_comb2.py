#!/usr/bin/python3

for i in range(100):
    print(('0' if i < 10 else '') + "{}".format(i), end=", " if i < 99 else '')

print()
