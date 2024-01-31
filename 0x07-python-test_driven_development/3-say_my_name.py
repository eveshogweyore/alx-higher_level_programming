#!/usr/bin/python3
"""This module houses the logic to say a user's name."""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first_name> <last_name>

    Paramaters
    ----------
    first_name : str
        The user's first name.
    last_name : str
        The user's last_name.

    Return
    ------
        Nothing.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
