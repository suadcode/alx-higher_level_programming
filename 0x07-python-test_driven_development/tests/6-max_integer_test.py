#!/usr/bin/python3
"""Unittest used for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
        A class for TestMaxInteger class
    """

    def test_negative(self):
        """
            Tests if function can give the highest negative
            integer
        """
        self.assertEqual(max_integer([-2, -4, -1, -5]), -1)

    def test_positive(self):
        """
            Tests if function can give the highest positive
            integer
        """
        self.assertEqual(max_integer([2, 4, 1, 5]), 5)

    def test_positive_float(self):
        """
            Tests if function can give the highest positive
            float
        """
        self.assertEqual(max_integer([2.75, 4.25, 1.25, 5.5]), 5.5)

    def test_neg_float(self):
        """
            Tests if function can give the highest negative
            float
        """
        self.assertEqual(max_integer([-2.75, -4.25, -1.25, -5.5]), -1.25)

    def test_char(self):
        """
            Tests if function can give the highest string
        """
        self.assertEqual(max_integer(['a', 'A', 'r', 'R']), 'r')

    def test_strings(self):
        """
            Tests if function can give the highest string
        """
        self.assertEqual(max_integer(['area', 'Aert', 'rain', 'Rad']), 'rain')
        self.assertEqual(max_integer('Zenith'), 't')

    def test_empty_str(self):
        """
            Test if function can handle empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_max_integer(self):
        """Check for the max_integer in the max_integer module"""

        self.assertEqual(max_integer([1, 4, 5, 3]), 5)
        self.assertEqual(max_integer([1]), 1)

    def test_if_negative_int_in_list(self):
        """Check for the negative interger in list function"""

        self.assertEqual(max_integer([0, -3, -2]), 0)

    def test_if_all_negative_interger(self):
        """Check whether all arguments are negative"""

        self.assertEqual(max_integer([-2, -4, -6, -19]), -2)

    def test_if_list_empty(self):
        """Check if list is empty"""

        self.assertIsNone(max_integer([]))

    def test_if_no_args(self):
        """Check if no args is provided"""

        self.assertIsNone(max_integer())

    def test_if_none_is_arg(self):
        """Check if none is provided"""

        self.assertRaises(TypeError, max_integer, None)

    def test_if_a_wrong_type_in_list(self):
        """Check if a wrong type is provided"""

        self.assertRaises(TypeError, max_integer, [1, 2, "Alx"])

    def test_if_float_is_in_list(self):
        """Check if float is provided"""

        self.assertEqual(max_integer([-1.4, 3.8, 3.9, 1.5]), 3.9)


if __name__ == "__main__":
    unittest.main()
