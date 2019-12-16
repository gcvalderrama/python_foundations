# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

import unittest


# [1,2,3,0]
def move(target, index, anchor):
    pivot = index
    while pivot < anchor - 1:
        temp = target[pivot]
        target[pivot] = target[pivot + 1]
        target[pivot + 1] = temp
        pivot += 1


def move_zeros(target):
    if not target or len(target) == 1:
        return target

    if len(list(filter(lambda x: x == 0, target))) == 0:
        return target

    anchor = len(target)
    while anchor >= 0:
        for index in range(0, anchor):
            if target[index] == 0:
                move(target, index, anchor)
                anchor -= 1
                break
        else:
            break
    return target


class Test(unittest.TestCase):

    def test_empty(self):
        result = move_zeros([])
        self.assertEqual([], result)

    def test_case(self):
        result = move_zeros([0, 1, 0, 3, 12])
        self.assertEqual([1, 3, 12, 0, 0], result)

    def test_case_a(self):
        result = move_zeros([0, 0, 0, 0, 12])
        self.assertEqual([12, 0, 0, 0, 0], result)
