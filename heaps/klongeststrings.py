import heapq
import unittest
import itertools


def k_longest(k, stream):
    min_heap = [(len(s), s) for s in stream[:k]]
    heapq.heapify(min_heap)
    for ns in stream[k:]:
        heapq.heappushpop(min_heap, (len(ns), ns))
    
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


class Test(unittest.TestCase):

    def test_longest(self):
        result = k_longest(3, ["keyboard", "book", "house", "terminology", "biology"])
        self.assertEqual(['biology', 'keyboard', 'terminology'], result)


if __name__ == "__main__":
    unittest.main()
