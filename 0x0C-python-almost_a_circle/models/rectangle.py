#!/usr/bin/python3
""" Module that implements the Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that implements the Base class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if width <= 0:
            raise TypeError("width must be > 0")
        if height <= 0:
            raise TypeError("height must be > 0")
        if x < 0:
            raise TypeError("x must be >= 0")
        if y < 0:
            raise TypeError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ value: the set width. """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is int:
            if width <= 0:
                raise ValueError("width must be greater > 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ value: the set height. """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be greater > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ value: the set value for x. """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ value: the set value for y. """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
