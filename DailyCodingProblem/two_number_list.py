import unittest


def two_numbers(data, target):
    state = dict()
    for item in data:
        if item in state:
            return True
        rest = target - item
        state[rest] = item

    return False


class Test(unittest.TestCase):

    def test_case_a(self):
        data = [10, 15, 3, 7]
        target = 17
        result = two_numbers(data, target)
        self.assertTrue(result)

    def test_case_b(self):
        data = [10, 15, 3, 7]
        target = 18
        result = two_numbers(data, target)
        self.assertTrue(result)

    def test_case_c(self):
        data = [10, 15, 3, 7]
        target = 19
        result = two_numbers(data, target)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()



