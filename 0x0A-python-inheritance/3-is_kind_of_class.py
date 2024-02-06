#!/usr/bin/python3
""" Module to check object type status. """


def is_kind_of_class(obj, a_class):
    """ Returns True is the object is an instance of,
        or if the object is an instance of a class that
        inherited from the specified class. Otherwise, False.

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
    return isinstance(obj, a_class)
