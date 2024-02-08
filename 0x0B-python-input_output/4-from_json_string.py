#!/usr/bin/python3
""" A module that handles returning JSON string object. """
import json


def from_json_string(my_str):
    """ Returns a JSON string object. """
    return json.loads(my_str)
