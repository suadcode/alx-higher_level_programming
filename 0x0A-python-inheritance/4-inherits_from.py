#!/usr/bin/python3
"""
This module contains the function 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    is the object an instance of a class that inherited
    (directly or indirectly) from the specified class
        Args:
            obj: the initial object
            a_class: the class
            Returns: True if the object is an instance that is
			 inherited, else False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
