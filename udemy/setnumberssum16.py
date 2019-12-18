import unittest


def count_sets(arr, target):
    state = dict()
    return recursive(arr, target, len(arr)-1, state)


def recursive(arr, total, i, state):
    key = '{}-{}'.format(total, i)
    if key in state:
        return state[key]

    if total == 0:
        result = 1
    elif total < 0:
        result = 0
    elif i < 0:
        result = 0
    elif total < arr[i]:
        result = recursive(arr, total, i-1, state)
    else:
        result = recursive(arr, total - arr[i], i-1, state) + recursive(arr, total, i-1, state)
    state[key] = result
    return result


class Test(unittest.TestCase):

    def test_case(self):
        arr = [2, 4, 6, 10]
        result = count_sets(arr, 16)
        self.assertEqual(2, result)
