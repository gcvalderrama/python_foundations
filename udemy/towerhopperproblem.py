import unittest

count = 0


def is_hoppable(towers):
    state = dict()
    return recursive(towers, 0, state)


def recursive(towers, index, state):
    global count

    if index in state:
        return state[index]

    count += 1
    if index >= len(towers):
        return True
    steps = towers[index]
    if steps == 0:
        return False
    responses = []
    for i in range(1, steps+1):
        responses.append(recursive(towers, index+i, state))
    state[index] = max(responses)
    return state[index]


class Test(unittest.TestCase):

    def test_dp(self):
        towers = [4, 2, 0, 0, 2, 0]
        result = is_hoppable(towers)
        self.assertEqual(True, result)

    def test_dp_false(self):
        towers = [4, 2, 0, 0, 2, 0, 0, 0]
        result = is_hoppable(towers)
        self.assertEqual(False, result)

    def test_dp_long(self):
        towers = [4, 2, 0, 0, 2, 0, 3, 4, 6, 0, 5]
        result = is_hoppable(towers)
        print(count)

