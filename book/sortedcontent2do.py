#  Sort the content of the a file based on second field, e.g.
#  Input file:
#  Jervie,12,M
#  Jaimy,11,F
#  Tony,23,M
#  Janey,11,F
#  Output file:
#  Jaimy,11,F
#  Janey,11,F
#  Jervie,12,M
#  Tony,23,M
#  don’t worry about open file, close file etc
#  1Gb for memory but 4Gb for file

import unittest


def merge_sort(data):
    if len(data) < 2:
        return data
    result = []

    mid = int(len(data) / 2)
    
    y = merge_sort(data[:mid])
    z = merge_sort(data[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)

    result += y
    result += z

    return result


def sort_large(target):
    pass


class Test(unittest.TestCase):
    def test_case(self):

        data = [
            ("Jervie", 12, "M"),
            ("Jaimy", 11, "F"),
            ("Tony", 23, "M"),
            ("Janey", 11, "F")]

        # result = sort_large(data)
        result = merge_sort([11, 15, 12, 10])
        print(result)



#  Jaimy,11,F
#  Janey,11,F
#  Jervie,12,M
#  Tony,23,M


