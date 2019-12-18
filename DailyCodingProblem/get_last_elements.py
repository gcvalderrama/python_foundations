import unittest
import heapq


def n_largest_element(data, target):
    n = 0
    while n < len(data):
        data[n] *= -1
        n += 1

    heapq.heapify(data)
    result = None
    for i in range(target):
        result = heapq.heappop(data)

    return -1 * result


class Test(unittest.TestCase):

    def test_case_a(self):
        data = [10, 15, 3, 7, 21, 45]
        target = 2
        result = n_largest_element(data, target)
        self.assertEqual(21, result)


if __name__ == "__main__":
    unittest.main()



