#!/usr/bin/python3
""" A module to append a string at the end of a text file. """


def append_write(filename="", text=""):
    """ Appends a string to the end of a text file. """
    with open(filename, "a", encoding="utf-8") as file_obj:
        file_obj.write(text)
        return len(text)
