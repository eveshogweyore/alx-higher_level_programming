#!/usr/bin/python3
""" A Rectangle class module. """


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

class Rectangle(BaseGeometry):
    """ A Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Called on object instantiation. """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
