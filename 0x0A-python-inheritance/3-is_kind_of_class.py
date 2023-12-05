#!/usr/bin/python3
""" This module contains the function 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    Looks if the object is an instance
        Args:
            obj: the initial object
            a_class: thte class to confirm the object
            Returns: True if object is an instance of class
                     or False if not
    """
    return isinstance(obj, a_class)
