import unittest
import collections


def check(magazine, letter):

    count_letters = collections.Counter(letter)
    for c in magazine:
        if c in count_letters:
            count_letters[c] -= 1
            if count_letters[c] == 0:
                del count_letters[c]
        if not count_letters:
            return True
    return False


class Test(unittest.TestCase):

    def test_case(self):
        letter = "abccddee"
        magazine = "abcbcsddasjkruiojklfalee"
        result = check(magazine, letter)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()