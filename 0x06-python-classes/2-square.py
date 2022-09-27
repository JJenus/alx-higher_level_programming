#!/usr/bin/python3
"""Module with one class square"""

class Square:
    """Square class initializes size of square
    
    Args:
        size (int): size of square
    Attributes:
        size (int): private size of size
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
