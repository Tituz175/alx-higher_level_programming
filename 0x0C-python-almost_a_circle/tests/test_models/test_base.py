#!/usr/bin/python3
"""The Unittest file for the base package"""


import unittest
from models.base import Base


class TestCase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)
        self.b4 = Base()

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b4.id, 3)
