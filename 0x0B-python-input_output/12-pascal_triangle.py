#!/usr/bin/python3
"""
An actual Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    a list of lists of integers is returned
        Args:
            n (int): the actual number of lists and digits
        Returns: list of lists are returned

    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
