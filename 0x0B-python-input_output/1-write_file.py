#!/usr/bin/python3
""" A module to write a string to a text file. """


def write_file(filename="", text=""):
    """ Write a string to a text file and return the number of
    character
    """
    with open(filename, "w", encoding="utf-8") as file_obj:
        file_obj.write(text)
        return len(text)
