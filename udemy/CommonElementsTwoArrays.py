import unittest
from collections import defaultdict


def get_common2(vector_a, vector_b):
    if not vector_a or not vector_b:
        return []

    pos_a = 0
    pos_b = 0

    len_a = len(vector_a)
    len_b = len(vector_b)
    result = []
    while pos_a < len_a and pos_b < len_b:
        if vector_a[pos_a] == vector_b[pos_b]:
            result.append(vector_a[pos_a])
            pos_a += 1
            pos_b += 1
        elif vector_a[pos_a] > vector_b[pos_b]:
            pos_b += 1
        else:
            pos_a += 1

    return result


def get_common(vector_a, vector_b):

    if not vector_a or not vector_b:
        return []

    state = defaultdict(lambda: 0)
    result = []
    for a in vector_a:
        state[a] += 1
    for b in vector_b:
        state[b] += 1
        if state[b] == 2:
            result.append(b)

    return result




class Test(unittest.TestCase):

    def test_case_a(self):
        A = [1, 3, 4, 6, 7, 9]
        B = [1, 2, 4, 5, 9, 10]
        result = get_common2(A, B)
        self.assertEqual([1, 4, 9], result)

    def test_case_b(self):
        list_b1 = [1, 2, 9, 10, 11, 12]
        list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
        result = get_common2(list_b1, list_b2)
        self.assertEqual([1, 2, 9, 10, 12], result)

    def test_case_c(self):
        list_c1 = [0, 1, 2, 3, 4, 5]
        list_c2 = [6, 7, 8, 9, 10, 11]
        result = get_common2(list_c1, list_c2)
        self.assertEqual([], result)


if __name__ == "__main__":
    unittest.main()

