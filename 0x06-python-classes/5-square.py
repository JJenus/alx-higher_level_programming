#!/usr/bin/python3
"""Square module with property setter and getter"""

class Square:
    """setter and getter and print square #
    Args:
        size (int): size of square
    Attributes:
        size (int): size of square
    """
    __size = 0

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: size of square"""
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

    def my_print(self):
        """Prints square of #
        Returns: None
        """
        if self.__size == 0:
            print()
            return None
        for i in range(self.__size):
            for x in range(self.__size):
                print('#', end="")
            print()
