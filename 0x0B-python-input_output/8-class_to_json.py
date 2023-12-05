#!/usr/bin/python3
"""
This contains a "class_to_json" function
"""


def class_to_json(obj):
    """the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object is returned"""
    return obj.__dict__
