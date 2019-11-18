import unittest


class Test(unittest.TestCase):

    def test_case_a(self):
        ar = [1] * 10
        del ar[8]
        self.assertEqual(9, len(ar))

    def test_case_max(self):
        ar = [1] * 10
        self.assertRaises(IndexError, lambda: ar[11])



