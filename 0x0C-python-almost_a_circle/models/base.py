#!/usr/bin/python3
""" A Base class module. """


class Base:
    """ The Base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor. """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
