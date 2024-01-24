#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module to create all functionalities for Square class."""


class Square:
    """A square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Square __init__ method.

        size : int
            Stores the size of a Square object.
        position : tuple
            Stores the coordinates of the Square object.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Parameters
        ----------
        value : tuple
            Coordinates (x, y) passed into the method.

        Setter method checks for the following errors:
        (1) TypeError: Checks if value is a tuple of two positive
        integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(msg)
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError(msg)
        else:
            self.__position = value

    def area(self):
        """Calculates the square area of square object.
        Returns
        -------
        int
            Square area of square object.
        """

        return self.__size**2

    def my_print(self):
        """Prints an actual square."""

        if (self.__size == 0):
            print()

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("{}".format(" "), end="")
            for k in range(self.__size):
                print("{}".format("#"), end="")
            print()
