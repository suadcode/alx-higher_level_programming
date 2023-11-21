#!/usr/bin/python3
"A class Square is defined."""


class Square:
    """A square is represented."""

    def __init__(self, size=0):
        """A new square is initialised.
        Args:
            size (int): The new square size.
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The current area of the square is returned."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """The == comparision to a Square is defined."""
        return self.area() == other.area()

    def __ne__(self, other):
        """The != comparison to a Square is defined."""
        return self.area() != other.area()

    def __lt__(self, other):
        """The < comparison to a Square is defined."""
        return self.area() < other.area()

    def __le__(self, other):
        """The <= comparison to a Square is defined."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """The > comparison to a Square is defined."""
        return self.area() > other.area()

    def __ge__(self, other):
        """The >= compmarison to a Square is defined."""
        return self.area() >= other.area()
