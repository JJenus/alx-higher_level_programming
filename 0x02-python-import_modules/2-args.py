#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    plural = 's' if len(argv)-1 != 1 else ''
    end = ':' if len(argv)-1 > 0 else '.'
    print("{} argument{}".format(len(argv)-1, plural+end))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
