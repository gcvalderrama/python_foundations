import unittest
import copy

# Example: Given a smaller string s and a bigger string b,
# design an algorithm to find all permutations of the shorter
# string within the longer one. Print the location of each
# permutation.


def perm(prefix, rest, result):
    for e in rest:
        new_rest = copy.copy(rest)
        new_prefix = copy.copy(prefix)
        new_prefix.append(e)
        new_rest.remove(e)
        if len(new_rest) == 0:
            result.append(new_prefix)
            continue
        perm(new_prefix, new_rest, result)


def generate_permutation(target):
    state = list()
    perm([], target, state)
    return state


def get_permutations(large, short):
    result = []
    for index in range(0, len(large), len(short)):
        temp = large[index:index + len(short)]
        for c in short:
            if c not in temp:
                break
        else:
            result.append((index, index + len(short)))

    return result


class Test(unittest.TestCase):

    def test_case(self):
        result = get_permutations("cbabadcbbabbcbabaabccbabc", "abc")
        print(result)

    def test_permutation(self):
        result = generate_permutation([1, 2, 3])
        print(result)
