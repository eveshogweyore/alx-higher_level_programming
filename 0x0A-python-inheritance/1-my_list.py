#!/usr/bin/python3
""" This module handles class inheritance. """


class MyList(list):
    """ Exhibits the behaviour of the list class. """

    def print_sorted(self):
        """ Prints a list in sorted order. """
        print(sorted(self))
