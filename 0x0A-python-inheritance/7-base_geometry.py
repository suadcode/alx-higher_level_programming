#!/usr/bin/python3
"""This module contains the function 6-base_geometry.py
"""


class BaseGeometry:
    """Class with public instance methods area and integer_validator"""
    def area(self):
        """Gives an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """the value is an integer greater than 0 is validated"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
