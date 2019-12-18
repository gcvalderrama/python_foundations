import unittest


#  There exists a staircase with N steps,
#  and you can climb up either 1 or 2 steps at a time.
#  Given N, write a function that returns the number of unique ways you can climb the staircase.
#  The order of the steps matters.

def num_ways(n, state: dict, steps):
    if n == 0 or n == 1:
        return 1
    else:
        if n not in state:
            total = 0
            for step in steps:
                if n - step >= 0:
                    total += num_ways(n-step, state, steps)
            state[n] = total
        return state[n]


def num_ways_button_up(n, steps):
    if n == 0 or n == 1:
        return 0
    nums = dict()
    nums[0] = 1
    anchor = max(steps)
    for i in range(1, n+1):
        total = 0
        for j in steps:
            if i - j >= 0:
                total += nums[i-j]
        nums[i] = total

        keys = list(nums.keys())

        for t in keys:
            if i - t > anchor:
                del nums[t]



    return nums[n]


class Test(unittest.TestCase):

    def test_stairs(self):
        result = num_ways(4, dict(), [1, 2])
        self.assertEqual(5, result)

    def test_stairs_bu(self):
        result = num_ways_button_up(4,  [1, 2])
        self.assertEqual(5, result)

    def test_stairs_bu_prune(self):
        result = num_ways_button_up(80,  [1, 2])
        self.assertEqual(37889062373143906, result)


if __name__ == "__main__":
    unittest.main()


