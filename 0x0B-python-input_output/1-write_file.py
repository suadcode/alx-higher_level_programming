#!/usr/bin/python3
"""This contains a write_file function """


def write_file(filename="", text=""):
    """Astring will be written by write_file into a text file.
        Args:
            filename (str): the name of file.
            text (str): the text to be written.
            Return: the number of characters written are returned
    """
    with open(filename, "w", encoding="utf-8") as file:
        files = file.write(text)
        return (files)
