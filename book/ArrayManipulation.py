import unittest
from collections import deque
import heapq


def arrayManipulationMem(n, queries):
    arr = [0 for i in range(n)]
    maximun = 0
    for item in queries:
        a = item[0] - 1
        b = item[1]
        value = item[2]
        for x in range(a, b):
            arr[x] += value
            maximun = max(arr[x], maximun)

    return maximun

def arrayManipulation(n, queries):
    maximum = 0
    current = 0

    starts = []
    ends = []

    for item in queries:
        starts.append((item[0], item[2]))
        ends.append((item[1], item[2]))

    heapq.heapify(starts)
    heapq.heapify(ends)

    while starts or ends:
        if starts and ends and starts[0][0] <= ends[0][0]:
            s = heapq.heappop(starts)
            current += s[1]
        else:
            e = heapq.heappop(ends)
            current -= e[1]
        maximum = max(maximum, current)

    return maximum


class Test(unittest.TestCase):

    def test_case(self):
        result = arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
        self.assertEqual(200, result)

    def test_case_b(self):
        result = arrayManipulation(5, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]])
        self.assertEqual(31, result)
