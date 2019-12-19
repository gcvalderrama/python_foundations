import unittest

#  What a fibonacci function which return N th position number both in recursive and loop,


def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)


def loop_fib(n):

    a = 0
    b = 1
    i = 2
    r = 0
    while i <= n:
        r = b + a
        a = b
        b = r

    return r


class Test(unittest.TestCase):

    def test_empty(self):
        result = recursive_fib(4)
        self.assertEqual(3, result)

    def test_loop(self):
        result = recursive_fib(4)
        self.assertEqual(3, result)
