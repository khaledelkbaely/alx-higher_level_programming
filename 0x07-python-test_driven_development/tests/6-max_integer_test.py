#!/usr/bin/python3
"""Unit test for max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test for max_integer function"""
    def test_no_arg(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([100]), 100)

    def test_identical(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([4, 4, 4, 4, 4]), 4)

    def test_max_start(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([4, 3, 2, 1, -1]), 4)

    def test_ordered(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_ordered_larger(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([4, 5, 7, 9, 12, 14, 15, 16, 18, 20]), 22)

    def test_unordered(self):
        """Unit test for max_integer function"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        self.assertRaises(TypeError, max_integer, ["a", "b", 9])

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        self.assertEqual(max_integer(["hi", "hello"]), "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)
