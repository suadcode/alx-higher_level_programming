#!/usr/bin/python3
""" Square module defined """


class Square:
    """ A square class is declared """

    def __init__(self, size=0) -> None:
        """
        The attributes are initialised

        Args:
            size: square size
        """
        self.size = size

    @property
    def size(self):
        """ Sets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes a square area """
        return self.__size ** 2
