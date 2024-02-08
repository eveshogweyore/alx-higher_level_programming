#!/usr/bin/python3
""" A module returns JSON representation of an object. """
import json

def to_json_string(my_obj):
    """ Returns object's JSON representation. """
    return json.dumps(my_obj)
