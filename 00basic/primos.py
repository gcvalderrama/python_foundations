import unittest


def is_prime(num):
    if num < 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


class Test(unittest.TestCase):

    def test_case_a(self):
        result = is_prime(10)
        self.assertFalse(result)

    def test_case_b(self):
        result = is_prime(1)
        self.assertTrue(result)


if __name__ == "__main__":
    print(is_prime(10))
