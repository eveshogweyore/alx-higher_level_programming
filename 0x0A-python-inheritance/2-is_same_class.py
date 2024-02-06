#!/usr/bin/python3
""" Module to check object type status. """


def is_same_class(obj, a_class):
    """ Returns True is the object is exactly an instance of
        the specified class. Otherwise, False.

        Parameters
        ----------
        obj : object
            The object to be checked for.
        a_class : objectType
            The class associated with the object.

        Returns
        -------
        On success, True. Othewise, False.
    """
    return type(obj) == a_class
