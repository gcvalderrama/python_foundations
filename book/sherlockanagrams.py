import unittest
from collections import defaultdict, deque, Counter
from itertools import combinations
import math
import copy


def bow(s, cache):

    if s in cache:
        return cache[s].copy()

    table = defaultdict(int)
    for c in s:
        table[c] += 1

    cache[s] = table.copy()
    return table


def is_anagram(a, b, cache):
    key = frozenset((a, b))
    if key in cache:
        return cache[key]

    result = True
    a_bow = bow(a, cache)
    for c in b:
        if c in a_bow and a_bow[c] > 0:
            a_bow[c] -= 1
        else:
            result = False
            break
    cache[frozenset((a, b))] = result
    cache[frozenset((b, a))] = result
    return result



def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def another(s: str):
    anagrams = 0
    n = len(s)
    words = defaultdict(list)
    one_book = Counter(s)
    cache = dict()

    for key, value in one_book.items():
        if value > 1:
            con = len(list(combinations([x for x in range(value)], 2)))
            anagrams += con

    for i in range(n):
        for j in range(i + 1, n + 1):
            lon = j - i
            if lon > 1:
                word = s[i: j]
                key = ''.join(word)
                words[lon].append(key)

    for lon, l_words in words.items():
        len_words = len(l_words)
        for index in range(len_words - 1):
            word = l_words[index]
            for test_index in range(index + 1, len_words):
                test = l_words[test_index]
                p = is_anagram(word, test, cache)
                if p:
                    anagrams += 1

    return anagrams


class Test(unittest.TestCase):

    def test_case_a(self):
        s = "abcd"
        result = another(s)
        self.assertEqual(0, result)

    def test_case(self):
        s = "abba"
        result = another(s)
        self.assertEqual(4, result)

    def test_case_c(self):
        s = "kkkk"
        result = another(s)
        self.assertEqual(10, result)

    def test_case_d(self):
        s = "ifailuhkqq"
        result = another(s)
        self.assertEqual(3, result)


    def test_case_e(self):
        s = "zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw"
        result = another(s)
        self.assertEqual(428, result)

    def test_case_f(self):
        s = "ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges"
        result = another(s)
        self.assertEqual(403, result)

    def test_case_g(self):
        s = "mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw"
        result = another(s)
        self.assertEqual(370, result)

    def test_case_h(self):
        s = "gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde"
        result = another(s)
        self.assertEqual(471, result)

    def test_case_i(self):
        s = "ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel"
        result = another(s)
        self.assertEqual(399, result)

import cProfile
import cProfile
import re

if __name__ == "__main__":
    # unittest.main()
    cProfile.run('unittest.main()')
