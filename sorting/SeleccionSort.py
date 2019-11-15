#  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSelectionSort.html
import unittest
from sorting.fixtures import basic_array


def selection_sort(array_list):
    for slot in range(len(array_list)-1, 0, -1):
        position = 0
        for location in range(1, slot + 1):
            if array_list[location] > array_list[position]:
                position = location

        temp = array_list[slot]
        array_list[slot] = array_list[position]
        array_list[position] = temp


class Test(unittest.TestCase):

    def test_case_a(self):
        list_input, list_result = basic_array()
        selection_sort(list_input)
        self.assertEqual(list_result, list_input)


if __name__ == "__main__":
    unittest.main()
