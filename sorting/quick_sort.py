#  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
import unittest
from sorting.fixtures import basic_array


def partition(array, low, high):
    index = low
    pivot = array[index]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot:
            left_mark = left_mark + 1
        while array[right_mark] >= pivot and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[index]
    array[index] = array[right_mark]
    array[right_mark] = temp

    return right_mark


def quick_sort(arr, begin, end):
    if begin < end:
        pi = partition(arr, begin, end)
        quick_sort(arr, begin, pi - 1)
        quick_sort(arr, pi + 1, end)


class Test(unittest.TestCase):

    def test_case_a(self):
        list_input, list_result = basic_array()
        quick_sort(list_input, 0, len(list_input) - 1)
        self.assertEqual(list_result, list_input)


if __name__ == "__main__":
    unittest.main()
