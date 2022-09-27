#!/usr/bin/python3
"""Square module"""

class Square:
    """Square with one method area
    Args:
        size (int): size of square
    Attributes:
        size (int):
    """
    def __init__(self, size=0):
        self.__self = size

    def area(self):
        """Area accepts no arg
        Return: size^2 #(area)
        """
        return self.__size ** 2
