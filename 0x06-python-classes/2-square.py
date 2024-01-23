#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module to create all functionalities for Square class."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Square __init__ method.

        size : int
            Store the size of a Square object.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
