#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Max in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_single_element(self):
        """Only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """All negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        """Mix of negative and positive"""
        self.assertEqual(max_integer([-1, 0, 3, -5]), 3)

    def test_duplicate_values(self):
        """List with duplicate max values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_identical_elements(self):
        """All same elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_no_argument(self):
        """No argument passed (default empty list)"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
