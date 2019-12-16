# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:
# def findKthLargest(nums, k):
#   # Fill this in.#
# print findKthLargest([3, 5, 2, 4, 6, 8], 3)

import heapq
import unittest


def find_k_largest(target, k):
    if not target:
        return None
    target = list(map(lambda x: x * -1, target))
    heapq.heapify(target)
    result = None
    for i in range(k):
        result = heapq.heappop(target)
    return -1 * result


class Test(unittest.TestCase):

    def test_empty(self):
        result = find_k_largest([], 3)
        self.assertIsNone(result)

    def test_case(self):
        result = find_k_largest([3, 5, 2, 4, 6, 8], 3)
        self.assertEqual(5, result)
