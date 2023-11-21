#!/usr/bin/python3
"""A MagicClass that does exactly the bytecode is defined"""

import math


class MagicClass:
    """A circle is represented."""

    def __init__(self, radius=0):
        """A MagicClass is initialised.
        Arg:
            radius (float or int): The new MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """The MagicClass area is returned."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """The MagicClass circumference is returned."""
        return (2 * math.pi * self.__radius)
