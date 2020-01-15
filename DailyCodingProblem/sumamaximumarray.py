import unittest


def detect_max(target: list):

    max_sum = 0
    current_sum = 0
    index = 0
    while index < len(target):
        current_sum = max(target[index],
                          current_sum + target[index])
        if current_sum > max_sum:
            max_sum = current_sum
        index += 1
    return max_sum


class Test(unittest.TestCase):

    def test(self):
        target = [34, -50, 42, 14, -5, 86]
        result = detect_max(target)
        self.assertEqual(137, result)
