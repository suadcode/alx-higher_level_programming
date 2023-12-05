#!/usr/bin/python3
"""
This module contains the function 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an actual instance of the specified class
        Args:
            obj: the initial object
            a_class: ther class to confirm with the object
            Returns: True if object is exactly the instance
                     or False if not
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
