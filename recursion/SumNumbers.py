import unittest


def list_sum(array_list):
    if len(array_list) == 1:
        return array_list[0]
    else:
        return array_list[0] + list_sum(array_list[1:])


class Test(unittest.TestCase):

    def test_case_a(self):
        result = list_sum([1, 3, 5, 7, 9])
        self.assertEqual(25, result)
        


if __name__ == "__main__":
    unittest.main()
