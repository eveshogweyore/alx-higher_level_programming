#!/usr/bin/python3
""" A module to test ```max_integer``` function. """
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_result(self):
        result = max_integer([10, 20, 30, 40])
        self.assertEqual(result, 40)
        result = max_integer([10, 30, 40, 20])
        self.assertEqual(result, 40)
        result = max_integer([40, 10, 30, 20])
        self.assertEqual(result, 40)
        result = max_integer([10, 40, -100, 30])
        self.assertEqual(result, 40)
        result = max_integer([-10, -20, -30, -40])
        self.assertEqual(result, -10)
        result = max_integer([10])
        self.assertEqual(result, 10)
        result = max_integer([])
        self.assertEqual(result, None)
