#!/usr/bin/python3
"""class module"""

class Square:
    """class Square
    Atttributes:
        size (int): size of square
        position (:obj:`tuple` of :obj:`int`): position
    """
    __size = 0
    __position = ()

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: size of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple
                or type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns: area of square"""
        return self.__size ** 2

    def my_print(self):
        """Returns: None"""
        if self.__size == 0:
            print()
            return None

        for i in range(self.__size):
            if self.__position[1] <= 0 or self.__position[1] == 1:
                for i in range(self.__position[0]):
                    print("_", end="")
            for x in range(self.__size):
                print('#', end="")
            print()
