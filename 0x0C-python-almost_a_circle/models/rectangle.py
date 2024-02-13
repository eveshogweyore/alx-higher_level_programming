#!/usr/bin/python3
""" Module that implements the Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that implements the Base class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ value: the set width. """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ value: the set height. """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ value: the set value for x. """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ value: the set value for y. """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
