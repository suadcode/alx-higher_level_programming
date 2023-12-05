#!/usr/bin/python3
"""
    A Module for class Student
"""


class Student:
    """
        Class students that defines a student by:
        Attributes:
            first_name (str): the name of student.
            last_name (str): the name of student.
            age (int): the actual age of student.
        Methods:
            __init__ - the Student instance will be initialized.
            to_json - dictionary repr of Student instance is retrieved.
    """
    def __init__(self, first_name, last_name, age):
        """
            Student instance is initialized.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            a dictionary representation of Student is retrieved.
            Args:
                attr (list): retrieve attribute names.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
