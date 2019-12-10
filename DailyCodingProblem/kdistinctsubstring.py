import unittest
import random
#  Given an integer k and a string s,
#  find the length of the longest substring that contains at most k distinct characters.


def count_unique(word):
    return len(set(word))


def right(word, budget, k, pos):
    if not (0 <= pos < len(word)):
        return budget
    if word[pos] in budget:
        budget += word[pos]
        return right(word, budget, k, pos + 1)
    if count_unique(budget) == k:
        return budget
    else:
        budget += word[pos]
        return right(word, budget, k, pos + 1)


def left(word, budget, k, pos):
    if not(0 <= pos < len(word)):
        return budget
    if word[pos] in budget:
        budget = word[pos] + budget
        return left(word, budget, k, pos - 1)
    elif count_unique(budget) == k:
        return budget
    else:
        budget = word[pos] + budget
        return left(word, budget, k, pos - 1)


def subs(word, k):

    result = ""
    for pos in range(len(word)):
        budget = ""
        r_result = right(word, budget, k, pos)
        l_result = left(word, budget, k, pos)
        result = max(r_result, l_result, result, key=lambda r: len(r))

    return result


class Test(unittest.TestCase):

    def test_monte_carlo(self):
        s = "abcba"
        k = 2
        result = subs(s, k)
        self.assertEqual("bcb", result)



if __name__ == "__main__":
    unittest.main()


