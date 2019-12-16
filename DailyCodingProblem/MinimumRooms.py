import unittest
import heapq


def schedule_rooms(intervals):
    if not intervals:
        return 0

    starts = list()
    ends = list()

    temp = list()
    for item in intervals:
        starts.append(item[0])
        ends.append(item[1])

    heapq.heapify(starts)
    heapq.heapify(ends)

    count = 0
    max_count = 0
    while starts or ends:
        if (starts and ends) and starts[0] <= ends[0]:
            count += 1
            heapq.heappop(starts)
            if count > max_count:
                max_count = count
        else:
            count -= 1
            heapq.heappop(ends)

    return max_count


class Test(unittest.TestCase):

    def test_empty(self):
        interval = []
        result = schedule_rooms(interval)
        self.assertEqual(0, result)

    def test_case(self):
        interval = [(30, 75), (0, 50), (60, 150)]
        result = schedule_rooms(interval)
        self.assertEqual(2, result)

    def test_case_b(self):
        interval = [(30, 75), (0, 50), (60, 150), (35, 40)]
        result = schedule_rooms(interval)
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
