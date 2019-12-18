import unittest


def sum_large(longest, shortest):
    index_l = len(longest) - 1
    index_s = len(shortest) - 1
    rest = 0
    result = ""

    while index_l >= 0 or index_s >= 0:
        temp = 0
        if index_l >= 0 and index_s >= 0:
            temp = int(longest[index_l]) + int(shortest[index_s])
        elif index_l >= 0:
            temp = int(longest[index_l])
        else:
            temp = int(shortest[index_s])

        if temp + rest >= 10:
            temp = (temp + rest - 10)
            rest = 1
        else:
            temp = temp + rest
            rest = 0

        result += str(temp)

        index_l -= 1
        index_s -= 1

    if rest > 0:
        result += str(rest)

    return result[::-1]


def aVeryBigSum(ar):
    result = "0"
    for x in ar:
        result = sum_large(result, str(x))
    return result


class Test(unittest.TestCase):

    def test_case(self):
        result = aVeryBigSum(["1000000001", "1000000002", "1000000003", "1000000004", "1000000005"])
        self.assertEqual("5000000015", result)

    def test_case_b(self):
        result = aVeryBigSum(["1", "999"])
        self.assertEqual("1000", result)
