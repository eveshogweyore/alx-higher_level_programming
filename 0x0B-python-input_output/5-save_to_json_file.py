#!/usr/bin/python3
""" A module that save an object to a file. """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file. """
    with open(filename, "w", encoding="utf-8") as file_obj:
        file_obj.write(json.JSONEncoder().encode(my_obj))
