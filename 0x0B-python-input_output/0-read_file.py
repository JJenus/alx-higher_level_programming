#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    """read file
    Args:
        filename (str): location/path
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read())
