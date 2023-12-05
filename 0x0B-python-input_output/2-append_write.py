#!/usr/bin/python3
"""The append text function is contained"""


def append_write(filename="", text=""):
    """a string is appended and the number of characters to be added will be returned"""
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.write(text)
        return lines
