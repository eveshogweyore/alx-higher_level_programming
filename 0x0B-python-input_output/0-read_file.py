#!/usr/bin/python3
""" A module to prints the content of a text file to stdout. """


def read_file(filename=""):
    """ Reads a text file's content to stdout. """
    with open(filename, encoding="utf-8") as file_obj:
        print(file_obj.read(), end="")
