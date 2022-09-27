#!/usr/bin/python3
"""Square module"""

class Square:
    """Square class
    Atrributes:
        size (int): size of square
    Args:
        size (int): private size
    """
    __size = 0

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns: area of square"""
        return self.__size ** 2
