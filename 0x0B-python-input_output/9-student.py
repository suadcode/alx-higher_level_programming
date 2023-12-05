#!/usr/bin/python3
"""
This contains class "Student"
"""


class Student:
    """A representation of a student"""
    def __init__(self, first_name, last_name, age):
        """The student is initialized"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A dictionary representation of a Student instance is returned"""
        return self.__dict__
