import unittest


def is_unique(target):

    temp = ""

    for c in target:
        if c in temp:
            return False
        else:
            temp += c
    return True


def check_permutation(str_a, str_b):
    longest = None
    shortest = None

    if len(str_a) >= len(str_b):
        longest = str_a
        shortest = str_b
    else:
        longest = str_b
        shortest = str_a

    shortest_map = dict()

    for item in shortest:
        shortest_map[item] = 1

    for item in longest:
        if item not in shortest_map:
            return False
    return True


class Test(unittest.TestCase):

    def test_unique_characters_true(self):
        target = "abcdfe"
        result = is_unique(target)
        self.assertTrue(result)

    def test_unique_characters_false(self):
        target = "abcdfeef"
        result = is_unique(target)
        self.assertFalse(result)

    def test_permutations(self):
        result = check_permutation("abcde", "abcdeabcdeabcdeabcdeabcde")
        self.assertTrue(result)



