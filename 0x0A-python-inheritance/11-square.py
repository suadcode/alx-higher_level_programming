#!/usr/bin/python3

""" The class that inherits from BaseGeometry """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the class Square that inherits """

    def __init__(self, size):
        """Initializing of the function
            Args:
                width: a rectangle breath
                height: a rectangle height
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Area of Calculator """
        return super().area()

    def __str__(self):
        """ info printed"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
