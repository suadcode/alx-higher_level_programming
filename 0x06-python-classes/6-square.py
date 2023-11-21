#!/usr/bin/python3
""" Square module is defined"""


class Square:
    """A square class is declared"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        The attributes are initialised

        Args:
            size: square size
            position:  square position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets the private attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Sets the private attribute to be used in class """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value     # tuple contains 2 positive integers

    def area(self):
        """Area of a square is printed """
        return self.__size ** 2

    def my_print(self):
        """ Prints square with the character # """
        if self.__size == 0:
            print()
        else:
            integer = 0
            pos1, pos2 = self.__position
            for new_line in range(pos2):
                print()
            while integer < self.__size:

                j = 0
                while j < pos1:
                    print(" ", end='')  # replace position with space
                    j += 1

                number = 0
                while number < self.__size:
                    print("{}".format("#"), end='')
                    number += 1
                print()
                integer += 1
