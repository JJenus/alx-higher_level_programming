#!/usr/bin/python3

for i in range(97, 123):
    if "{i:c}".format(i=i) == 'q' or "{i:c}".format(i=i) == 'e':
        continue
    print("{i:c}".format(i=i), end='')
