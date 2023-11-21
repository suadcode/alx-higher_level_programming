#!/usr/bin/python3
""" Square module defined"""


class Square:
    """ A square class is declared """

    def __init__(self, size) -> None:
        """
        Class attributes are initialised

        Args:
            size: The actual size of the square
        """
        self.__size = size
