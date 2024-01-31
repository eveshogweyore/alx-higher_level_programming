#!/usr/bin/python3
"""Module to handle logic associated with dividing a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Parameters
    ----------
    matrix : list
        The lists of lists to be divided by a certain number.
    div : int
        The divisor.

    Returns
    -------
        If successful, new list with the result of division.
        Otherwise, error is raised.
    """
    new_list = []
    idx = 0
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == float("inf") or div == float("-inf"):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError(err)

    length = len(matrix[0])

    for inner_list in matrix:
        new_list.append([])
        if length != len(inner_list):
            raise TypeError("Each row of the matrix must have the same size")
        for j in inner_list:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(err)
            new_list[idx].append(round(j/div, 2))

        idx += 1

    return new_list
