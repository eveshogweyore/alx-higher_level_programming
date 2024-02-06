#!/usr/bin/python3
""" A module to check if an object inherits from a class. """


def inherits_from(obj, a_class):
    """ A function that checks if an object inherits from a class

    Parameters
    ----------
    obj : object
        The object to be checked for.
    a_class : objectType
        The class associated with the object.

    Returns
    -------
        On success, True. Otherwise, False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
