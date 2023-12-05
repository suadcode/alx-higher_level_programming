#!/usr/bin/python3
"""
The container of MyList class that inherits from list
"""


class MyList(list):
    """MyList class that inherits"""
    def __init__(self):
        """Used to initialize the object"""
        super().__init__()

    def print_sorted(self):
        """This will print the sorted list"""
        print(sorted(self))
