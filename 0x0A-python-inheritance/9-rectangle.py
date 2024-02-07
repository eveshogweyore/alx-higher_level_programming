#!/usr/bin/python3
""" A Rectangle class module. """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Called on object instantiation. """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ Returns the area of a rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """Human-readable representation of Rectangle class."""
        return f"[Rectangle] {self.__width}/{self.__height}"
