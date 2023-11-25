#!/usr/bin/python3
"""
    The 4-print_square Module
"""


def print_square(size):
    """
        A square with the character '#' is printed

        Args:
            size: size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
