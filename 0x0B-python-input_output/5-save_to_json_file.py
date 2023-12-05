#!/usr/bin/python3
"""
This contains the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """an Object to a text file, using a JSON representation is written"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
