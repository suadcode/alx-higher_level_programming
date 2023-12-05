#!/usr/bin/python3

"""A Class that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The representation of a rectangle"""

    def __init__(self, width, height):
        """
        Function is inintialized
            Args:
                width: the rectangle breath
                height: the rectangle length
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """the rectangle area is returned"""
        return self.__width * self.__height

    def __str__(self):
        """An informal string of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
