#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print(f"{len(argv)-1} arguments")
    for i in range(1, len(argv)):
        print(f"{i}. {argv[i]}")
