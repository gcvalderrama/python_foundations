import unittest
import heapq


def minimumSwaps(arr):
    movements = 0
    n = len(arr)
    delta = 0
    state = dict()
    for index in range(n):
        state[arr[index]] = index

    for target in range(n, 0, -1):
        end = n - 1 - delta
        pos = state[target]

        if end != pos:
            temp = arr[end]
            arr[end] = arr[pos]
            arr[pos] = temp

            state[target] = end
            state[temp] = pos

            movements += 1

        delta += 1

    return movements


class Test(unittest.TestCase):

    def test_case(self):
        arr = [4, 3, 1, 2]
        d = minimumSwaps(arr)
        self.assertEqual(3, d)

    def test_case_b(self):
        arr = [1, 3, 5, 2, 4, 6, 7]
        d = minimumSwaps(arr)
        self.assertEqual(3, d)


if __name__ == "__main__":
    unittest.main()