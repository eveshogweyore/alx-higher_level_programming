#!/usr/bin/python3
""" A Base class module. """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
