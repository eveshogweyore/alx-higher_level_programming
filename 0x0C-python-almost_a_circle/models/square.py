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
