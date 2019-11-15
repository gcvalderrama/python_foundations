#  https://www.geeksforgeeks.org/insertion-sort/
#  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
#  Time Complexity: O(n*2)
#  Auxiliary Space: O(1)
import unittest
from .fixtures import basic_array


def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i - 1
        nxt_element = input_list[i]
        # Compare the current element with next one
        while (input_list[j] > nxt_element) and (j >= 0):
            input_list[j + 1] = input_list[j]
            j = j - 1
        input_list[j + 1] = nxt_element


class Test(unittest.TestCase):

    def test_case_a(self):
        list_input, list_result = basic_array()
        insertion_sort(list_input)
        self.assertEqual(list_result, list_input)


if __name__ == "__main__":
    unittest.main()

