import unittest
from collections import defaultdict


def is_rotate(str_a, str_b):
    if len(str_a) != len(str_b):
        return False

    state = defaultdict(int)
    for index in range(len(str_b)):
        state[str_a[index]] += 1
        state[str_b[index]] -= 1

    for k, v in state.items():
        if v != 0:
            return False

    for pivot in range(len(str_b)):

        pivot_a = 0
        pivot_b = pivot

        for i in range(len(str_a)):
            if str_a[pivot_a] != str_b[pivot_b]:
                break

            pivot_a += 1
            pivot_b = (pivot_b + 1) % len(str_b)
        else:
            return True

    return False


def is_inverse(str_a, str_b):

    if len(str_a) != len(str_b):
        return False

    pivot_a = 0
    pivot_b = len(str_a) - 1

    while pivot_a < len(str_a):
        if str_a[pivot_a] != str_b[pivot_b]:
            return False
        pivot_a += 1
        pivot_b -= 1

    return True


class Test(unittest.TestCase):

    def test_case(self):
        result = is_inverse("waterbottle", "elttobretaw")
        self.assertTrue(result)

    def test_rotate(self):
        result = is_rotate("waterbottle", "erbottlewat")
        self.assertTrue(result)

    def test_rotate_false(self):
        result = is_rotate("waterbottlea", "erbottlewati")
        self.assertFalse(result)
