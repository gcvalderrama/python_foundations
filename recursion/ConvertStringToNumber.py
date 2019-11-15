import unittest
from collections import deque


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]


def to_str_stack(n, base):
    convert_string = "0123456789ABCDEF"
    stack = deque()

    while n > 0:
        if n < base:
            stack.append(convert_string[n])
        else:
            stack.append(convert_string[n % base])
        n = n // base
    res = ""

    while len(stack):
        res = res + str(stack.pop())

    return res


class Test(unittest.TestCase):

    def test_case_a(self):
        result = to_str(1453, 16)
        self.assertEqual("5AD", result)

    def test_case_b(self):
        result = to_str_stack(1453, 16)
        self.assertEqual("5AD", result)


if __name__ == "__main__":
    unittest.main()
