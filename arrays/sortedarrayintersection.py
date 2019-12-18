import unittest


def intersect(a, b):
    result = []
    i_a = 0
    i_b = 0

    while i_a < len(a) and i_b < len(b):
        if a[i_a] == b[i_b]:
            if a[i_a] not in result:
                result.append(a[i_a])
            i_a += 1
            i_b += 1
        elif a[i_a] <= b[i_b]:
            i_a += 1
        else:
            i_b += 1

    return result


class Test(unittest.TestCase):

    def test_case(self):
        a1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
        a2 = [5, 5, 6, 8, 8, 9, 10, 10]
        result = intersect(a1, a2)
        self.assertEqual([5, 6, 8], result)


if __name__ == "__main__":
    unittest.main()
