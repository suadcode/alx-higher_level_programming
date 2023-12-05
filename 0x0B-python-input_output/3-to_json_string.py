#!/usr/bin/python3
"""
This is a condition for the  "to_json_string" function
"""

import json


def to_json_string(my_obj):
    """The JSON representation of an object (string) is returned"""
    return json.dumps(my_obj)
