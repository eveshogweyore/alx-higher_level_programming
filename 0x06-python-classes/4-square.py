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
        self.size = size

    @property
    def size(self):
        """
            Parameter
            ---------
            value : int
                New value to be set as size of Square object.
            Returns
            -------
            int
                size of Square object

            Setter method checks for the following errors:
            (1) TypeError: Checks if value is an integer.
            (2) ValueError: Checks is value is less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square area of square object.
        Returns
        -------
        int
            Square area of square object.
        """

        return self.__size**2
