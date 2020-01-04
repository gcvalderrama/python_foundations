#  Swap two digits from an integer,
#  the result should be the maximum.
#  For example 3580 -> 8350

import unittest


def swap_numbers(target):
    res = 0
    temp = target
    result = list()
    while temp > 0:
        res = temp % 10
        temp = (temp - res) / 10
        result.append(res)

    result = sorted(result)

    response = 0
    pivot = 1
    for index in range(len(result)):
        response += result[index] * pivot
        pivot = pivot * 10

    return response


class Test(unittest.TestCase):

    def test_case(self):
        result = swap_numbers(3580)
        self.assertEqual(8530, result)


