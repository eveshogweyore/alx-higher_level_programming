#!/usr/bin/python3
""" A module to improve on the BaseGeometry class. """


class BaseGeometry:
    """ A BaseGeometry class."""

    def area(self):
        """ A method that raises an exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks if the the values passed are valid. """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
