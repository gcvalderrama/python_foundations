import unittest


def kangaroo(x1, v1, x2, v2):

    if x1 == x2 and v1 == v2:
        return 'YES'

    fast, fast_step = (x1, v1) if v1 >= v2 else (x2, v2)
    slow, slow_step = (x1, v1) if v1 < v2 else (x2, v2)

    if (fast > slow) or (fast_step == slow_step):
        return 'NO'

    steps = abs(fast - slow) // fast_step
    print(steps)
    fast = fast + (fast_step * steps)
    slow = slow + (slow_step * steps)

    while fast < slow:
        fast = fast + fast_step
        slow = slow + slow_step

    return 'YES' if fast == slow else 'NO'

class Test(unittest.TestCase):

    def test_case_a(self):
        print( 2 % 4)
        result = kangaroo(43, 2, 70, 2)
        self.assertEqual('NO', result)
