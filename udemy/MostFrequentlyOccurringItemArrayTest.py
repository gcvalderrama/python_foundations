import unittest


def most_frequent(data):
    if not data:
        return None
    max_number = max_count = 0
    numbers = dict()

    for i in data:
        if i not in numbers:
            numbers[i] = 1
        else:
            numbers[i] = numbers[i] + 1

        if numbers[i] > max_count:
            max_number = i
            max_count = numbers[i]

    return max_number


class Test(unittest.TestCase):

    def test_case_a(self):
        list_input = [1, 3, 1, 3, 2, 1]
        result = most_frequent(list_input)
        self.assertEqual(1, result)

    def test_case_b(self):
        list_input = [3, 3, 1, 3, 2, 1]
        result = most_frequent(list_input)
        self.assertEqual(3, result)

    def test_case_c(self):
        list_input = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
        result = most_frequent(list_input)
        self.assertEqual(-1, result)

    def test_case_d(self):
        list_input = []
        result = most_frequent(list_input)
        self.assertEqual(None, result)


if __name__ == "__main__":
    unittest.main()
