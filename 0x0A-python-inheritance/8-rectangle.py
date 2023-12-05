#!/usr/bin/python3
"""This module contains the function 7-base_geometry.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of a rectangle and
       Class that will inherit from BaseGeometry
    """
    def __init__(self, width, height):
        """function initialized
            Args:
                width: the actual variable to be initialized
                height: the actual variable to be initialized
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
