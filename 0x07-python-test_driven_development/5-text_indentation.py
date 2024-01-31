#!/usr/bin/python3
"""Module containing logic to indent text."""


def text_indentation(text):
    """Prints a text with 2 new lines after some characters.

    Parameters
    ----------
    text : str
        The text to be parsed.

    Return
    ------
        Nothing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    last_char = ""
    for char in text:
        if last_char in (".", "?", ":"):
            last_char = char
            continue

        print(char, end="")

        if char in (".", "?", ":"):
            print("\n")

        last_char = char
