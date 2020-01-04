import unittest
from collections import defaultdict, deque
import sys


def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):

        d = (val - 1) - pos
        if d > 2:
            return "Too chaotic"
        start = max(0, val - 2)
        end = pos + 1
        for j in range(start, end):
            if q[j] > val:
                moves += 1
    return moves

def minimumBribesa(final):
    n = len(final)
    queue = [i for i in range(1, n + 1)]

    state = defaultdict(int)
    n = len(final)
    for index in range(n):
        state[final[index]] = index

    movements = 0
    ite = deque(queue[:])
    while ite:
        target = ite.popleft()
        pos = state[target]
        index = queue.index(target)
        dist = abs(pos - index)
        if dist > 2:
            return "Too chaotic"
        while queue[pos] != target:
            movements += 1
            temp = queue[index + 1]
            queue[index + 1] = target
            queue[index] = temp
            index = index + 1

    return movements


class Test(unittest.TestCase):

    def test_case(self):
        peaple = 5
        target = [2, 1, 5, 3, 4]
        result = minimumBribes(target)
        self.assertEqual(3, result)

    def test_case_caotic(self):
        peaple = 5
        target = [2, 5, 1, 3, 4]
        result = minimumBribes(target)
        self.assertEqual("Too chaotic", result)

    def test_case_caotic_b(self):
        target = [5, 1, 2, 3, 7, 8, 6, 4]
        result = minimumBribes(target)
        self.assertEqual("Too chaotic", result)

    def test_case_caotic(self):
        #arget = [1, 2, 3, 4, 5, 6, 7, 8]
        target = [1, 2, 5, 3, 7, 8, 6, 4]
        result = minimumBribes(target)
        self.assertEqual(7, result)

