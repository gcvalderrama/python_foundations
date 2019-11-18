#  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
#  https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
from .fixtures import basic_array
import unittest


def sort(input_list):
    for iter_number in range(len(input_list) - 1, 0, -1):
        for idx in range(iter_number):
            if input_list[idx] > input_list[idx+1]:
                temp = input_list[idx]
                input_list[idx] = input_list[idx + 1]
                input_list[idx + 1] = temp


class Test(unittest.TestCase):

    def test_case_a(self, ):
        list_input, list_result = basic_array()
        sort(list_input)
        self.assertEqual(list_result, list_input)


