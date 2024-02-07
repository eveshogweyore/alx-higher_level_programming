#!/usr/bin/python3
""" A Square module."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A Square class. """
    def __init__(self, size):
        """ Method to be called on class instantiation. """
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """ Calculates the area of a square. """
        return self.__size ** 2

    def __str__(self):
        """ Human-readable representation of Square class. """
        return f"[Square] {self.__size}/{self.__size}"
