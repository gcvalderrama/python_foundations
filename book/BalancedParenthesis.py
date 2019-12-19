import unittest
from collections import deque


def balanced(target):
    state = deque()
    metadata = dict()
    metadata["("] = ")"
    metadata["["] = "]"
    metadata["{"] = "}"

    for item in target:
        if item in metadata.keys():
            state.append(item)
        elif item in metadata.values():
            temp = state.pop()
            if metadata[temp] != item:
                return False
    return len(state) == 0


class Test(unittest.TestCase):

    def test_case_a(self):
        result = balanced("a(bcd)d")
        self.assertTrue(result)

    def test_case_b(self):
        result = balanced("(kjds(hfkj)sdhf")
        self.assertFalse(result)

    def test_case_c(self):
        result = balanced("(sfdsf)(fsfsf")
        self.assertFalse(result)

    def test_case_d(self):
        result = balanced("{[]}()")
        self.assertTrue(result)

    def test_case_e(self):
        result = balanced("{[}]")
        self.assertFalse(result)


