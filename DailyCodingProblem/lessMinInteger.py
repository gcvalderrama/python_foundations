# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does
# not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example,
# the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.

import unittest
import sys


def min_number(data):
    if not data:
        return None

    data = filter(lambda d: d > 0, data)

    min_integer = sys.maxsize

    state = dict()

    for item in data:
        state[item] = 1
        if item < min_integer:
            min_integer = item

    pivot = min_integer
    while pivot > 0:  # 0 is valid?
        if pivot not in state:
            min_integer = pivot
            break
        pivot -= 1
    else:
        while True:
            if min_integer not in state:
                break
            min_integer += 1

    return min_integer


class Test(unittest.TestCase):

    def test_case_empty(self):
        result = min_number([])
        self.assertFalse(result)

    def test_case_one(self):
        data = [3, 4, -1, 1]
        result = min_number(data)
        self.assertEqual(2, result)

    def test_case_two(self):
        data = [1, 2, 0]
        result = min_number(data)
        self.assertEqual(3, result)

    def test_case_c(self):
        data = [-2, 1, 2, 0, -1]
        result = min_number(data)
        self.assertEqual(3, result)

    def test_case_d(self):
        data = [-2, 2, 4, -1]
        result = min_number(data)
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
