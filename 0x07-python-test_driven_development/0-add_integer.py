#!/usr/bin/python3
""" This module contains functionality to add two digits."""

def add_integer(a, b=98):
    """Function to add two integer  values.

    Parameters
    ----------
    a : int
        First of the two integers.
    b : int
        Second of the two integers.

    Returns
    -------
    int
        The result of the addition of both integer values.
        Otherwise, type error is raised.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
