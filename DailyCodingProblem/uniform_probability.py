import unittest
import random
# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.
# https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/
# https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/


count = 0
res = 0


def get_random(target):
    global count
    global res
    count = count + 1
    if count == 1:
        res = target
    else:
        i = random.randrange(count)
        if i == count - 1:
            res = target
    return res


def pick(array):
    result = list()
    for i in array:
        result.append(get_random(i))
    return result


class Test(unittest.TestCase):

    def test_monte_carlo(self):
        print(pick([1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()


