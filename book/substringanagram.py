#  We have two words. We need to determine if the second word contains
#  a substring with an anagram of the first word

import unittest


def anagram_substring(target, base):

    if not base or not target:
        return False

    state = dict()
    for c in base:
        state[c] = 1

    for c in target:
        if c not in state:
            return False

    return True


class Test(unittest.TestCase):

    def test_case(self):
        result = anagram_substring("board", "keyboard")
        self.assertTrue(result)

