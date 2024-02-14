#!/usr/bin/python3
""" A module that implements the Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from the Rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Human-readable representation of Square class. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ value: the new set width and height for square. """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.width = value
            self.height = value
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """ Square implementation of update method. """
        if len(args) > 0:
            instance_var = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, instance_var[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
