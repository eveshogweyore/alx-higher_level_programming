#!/usr/bin/python3
""" A module that creates an Object from a JSON file. """
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file. """
    with open(filename, encoding="utf-8") as file_obj:
        return json.loads(file_obj.read())
