#!/usr/bin/python3
"""
This Contains the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """an Object from a "JSON file" is created"""
    with open(filename, 'r', encoding='utf-8') as file:
        create_obj = json.load(file)
        return create_obj
