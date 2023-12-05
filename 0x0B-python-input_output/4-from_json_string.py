#!/usr/bin/python3
"""
This contains a "from_json_string" function
"""

import json


def from_json_string(my_str):
    """An object represented by a JSON string is returned"""
    return json.loads(my_str)
