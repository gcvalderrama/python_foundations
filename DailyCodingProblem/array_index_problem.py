import unittest
from functools import reduce


def dot(data):
    result = list()

    total = reduce(lambda x, y: x*y, data)

    for ix in range(len(data)):
        result.append(total / data[ix])

    return result


class Test(unittest.TestCase):

    def test_case_a(self):
        data = [1, 2, 3, 4, 5]
        target = [120, 60, 40, 30, 24]
        result = dot(data)
        self.assertEqual(target, result)

    def test_case_b(self):
        data = [3, 2, 1]
        target = [2, 3, 6]
        result = dot(data)
        self.assertEqual(target, result)


if __name__ == "__main__":
    unittest.main()
