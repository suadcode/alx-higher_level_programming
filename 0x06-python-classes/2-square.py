#!/usr/bin/python3
""" Square module is defined """


class Square:
    """ A square class is declared """

    def __init__(self, size=0) -> None:
        """
        Class attributes are initialised

        Args:
            size:  square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
