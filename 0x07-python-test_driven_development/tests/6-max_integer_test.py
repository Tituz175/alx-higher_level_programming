#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_max_integer_integer(self):
        """Test of max_integer on integer values"""
        self.assertEqual(max_integer([1, 2, 30, -2, -5]), 30)
        self.assertEqual(max_integer([1, 2, 30, 50]), 50)
        self.assertEqual(max_integer([100, 2, 30, 50]), 100)
        self.assertEqual(max_integer([-1, -2, -30, -2, -5]), -1)
        self.assertEqual(max_integer([60]), 60)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_float(self):
        """Test of max_integer on float values"""
        self.assertEqual(max_integer([1.0, 2.0, 30.4, -0.5, -5.0]), 30.4)
        self.assertEqual(max_integer([1.3, 2.05, 30.2, 50.5]), 50.5)
        self.assertEqual(max_integer([100.3, 2.05, 30.2, 50.5]), 100.3)
        self.assertEqual(max_integer([2.05]), 2.05)
        self.assertEqual(max_integer([-1.3, -2.44, -30.5, -2.3, -5.4]), -1.3)

    def test_max_integer_strings(self):
        """Test of max_integer on string values"""
        self.assertEqual(max_integer(["Tobi", "Praise", "Oyekanmi"]), "Tobi")
        self.assertEqual(max_integer(["i", "P", "r", "O"]), "r")
        self.assertEqual(max_integer("Praise"), "s")
        self.assertEqual(max_integer(""), None)

    def test_max_integer_mixture(self):
        """Test of max_integer on mixed values"""
        self.assertEqual(max_integer([100, 50.5]), 100)


if __name__ == '__main__':
    unittest.main()
