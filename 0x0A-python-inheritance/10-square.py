#!/usr/bin/python3
"""
This contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square class
        Args:
            size: the actual square
    """
    def __init__(self, size):
        """the square is initialised"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"the area of the square is returned"""
        return self.__size ** 2
