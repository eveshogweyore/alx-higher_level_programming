#!/usr/bin/python3
"""Module to handle logic to print a square."""


def print_square(size):
    """Prints a square with the character #.

    Parameter
    ---------
    size : int
        The size of the square.

    Return
    ------
        Nothing.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
