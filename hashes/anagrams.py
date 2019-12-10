import unittest
import collections


def find_anagrams(array):
    sorted_anagrams = collections.defaultdict(list)
    for s in array:
        sorted_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_anagrams.values() if len(group) >= 2
    ]


class Test(unittest.TestCase):

    def test_anagrams(self):
        target = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom",
                  "listen", "levis", "money"]
        result = find_anagrams(target)
        self.assertEqual(3, len(result))

