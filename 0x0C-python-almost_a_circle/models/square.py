#!/usr/bin/python3
"""A square class is defined."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is represented."""

    def __init__(self, size, x=0, y=0, id=None):
        """A new Square is initialized.

        Args:
            size (int): The size of the new Square.
            x (int): coordinate of the new Square.
            y (int): coordinate of the new Square.
            id (int): identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set the Square Size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The Square is updated.

        Args:
            *args (ints): Attribute values.
                - 1st arg stands for id attribute
                - 2nd arg stands for size attribute
                - 3rd arg stands for x attribute
                - 4th arg stands for y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
