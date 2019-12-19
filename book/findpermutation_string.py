import unittest


def find(target):
    hash = dict()
    for item in target:
        hash[item] = 1

    return hash


state = list()


def find_permutations(target):
    global state

    if not state:
        state.append(find(target))
        return 0

    for item in state:
        for c in target:
            if c not in item:
                break
        else:
            break
    else:
        state.append(find(target))
        return 0

    return 1


class Test(unittest.TestCase):

    def test_case(self):
        result = find_permutations("house")
        result = find_permutations("house")
        result = find_permutations("casa")
        result = find_permutations("casa")

        print(result)


if __name__ == "__main__":
    pass
