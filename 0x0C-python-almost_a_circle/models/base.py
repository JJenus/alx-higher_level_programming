#!/usr/bin/python3
"""Goto module """


class Base:
    """ Base class
    Args:
        @id (int): defaults to None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
