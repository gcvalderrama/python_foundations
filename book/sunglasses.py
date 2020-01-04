import unittest

def navigation(rows, cols, x, y):
    if 1 <= x <= rows - 2 and 1 <= y <= cols - 2:
        return [(x - 1 , y - 1), ( x - 1, y), ( x - 1, y + 1),
                                 ( x ,    y),
                (x + 1 , y - 1), ( x + 1, y), ( x + 1, y + 1)]

    return []

def hourglassSum(arr):
    if not arr:
        return 0
    rows = len(arr)
    cols = len(arr[0])
    maximun = -10000000
    for i in range(1, rows):
        for j in range(1, cols):
            temp = navigation(rows, cols, i, j)
            acc = -10000000
            for pivot in temp:
                acc += arr[pivot[0]][pivot[1]]
            maximun = max(acc, maximun)
    return maximun

class Test(unittest.TestCase):

    def test_case(self):
        arr = [[-1, -1, 0, -9, -2, -2],
               [-2, -1, -6, -8, -2, -5],
               [-1, -1, -1, -2, -3, -4],
               [-1, -9, -2, -4, -4, -5],
               [-7, -3, -3, -2, -9, -9],
               [-1, -3, -1, -2, -4, -5]]
        result = hourglassSum(arr)
        print(result)




