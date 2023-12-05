#!/usr/bin/python3
"""
This contains the lookup function
"""


def lookup(obj):
    """
    Args:
        obj: the initial object
        Returns: a list of available attributes along with
                 methods of an object
    """
    return dir(obj)
