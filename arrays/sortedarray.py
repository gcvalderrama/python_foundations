import unittest
#  https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

def first(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)

    return -1


def first_sorted_array(arr, k):
    n = len(arr)
    index = first(arr, 0, n-1, k, n)
    return index


class Test(unittest.TestCase):

    def test_first_last(self):
        arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
        result = first_sorted_array(arr, 5)
        self.assertEqual(2, result)
