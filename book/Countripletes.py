import math
import sys
import unittest
import cProfile
from itertools import combinations
from collections import defaultdict, deque


def read(name):
    with open(name, 'r') as fptr:
        nr = fptr.readlines()
        one = nr[0].split()
        n = int(one[0])
        r = int(one[1])
        arr = nr[1].split()
        arr = list(map(lambda x: int(x), arr))
        return arr, r


def factorial(n):

    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def nCr(n,r):
    f = math.factorial
    return factorial(n) / factorial(r) / factorial(n-r)

def countTriplets(arr, r):

    arr.sort()
    state = defaultdict(list)
    for index, value in enumerate(arr):
        if value % r == 0:
            state[value].append(index)

    result = 0
    for index, value in enumerate(arr):
        target = value
        budget = []
        for i in range(1, 3):
            target *= r
            if target in state:
                temporal = list(filter(lambda x: x > index, state[target]))
                budget.append(len(temporal))
            else:
                break
        else:
            result += budget[0] * budget[1]

    return result


class Test(unittest.TestCase):

    def test_case(self):
        result = countTriplets([1, 2, 2, 4], 2)
        self.assertEqual(2, result)

    def test_case_b(self):
        result = countTriplets([1, 3, 9, 9, 27, 81], 3)
        self.assertEqual(6, result)

    def test_case_c(self):
        result = countTriplets([1, 5, 5, 25, 125], 5)
        self.assertEqual(4, result)

    def test_case_e(self):
        arr, r = read('./count_t.txt')
        result = countTriplets(arr, r)
        self.assertEqual(166661666700000, result)

    def test_case_read(self):
        arr, r = read('./count_t.txt')
        self.assertEqual(len(arr), 100000)
        self.assertEqual(r, 1)


if __name__ == '__main__':
    unittest.main()
