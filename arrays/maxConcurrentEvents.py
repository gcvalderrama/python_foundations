import unittest
import collections

Event = collections.namedtuple('Event', ('start', 'finish'))
EndPoint = collections.namedtuple("Endpoint", ('time', 'is_start'))


def max_concurrent(a):
    end_points = ([EndPoint(event.start, True) for event in a] +
                  [EndPoint(event.finish, False) for event in a])

    end_points.sort(key=lambda c: (c.time, not c.is_start))
    max_num_events, num_events = 0, 0
    for e in end_points:
        if e.is_start:
            num_events += 1
            max_num_events = max(max_num_events, num_events)
        else:
            num_events -= 1
    return max_num_events


class Test(unittest.TestCase):

    def test_case(self):
        a = [Event(1, 5), Event(2, 7), Event(4, 5), Event(6, 10), Event(9, 17), Event(8, 9),
             Event(11, 13), Event(12, 15), Event(14, 15)]
        result = max_concurrent(a)
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
