#!/usr/bin/python
""" A module to handle object lookups. """


def lookup(obj):
    """ Returns the list of available attributes and methods
        of an object.

    Parameters
    ----------
    obj : object
        The object to be looked up.

    Returns
    -------
        A list of all attributes and method of an object.
    """
    return dir(obj)
