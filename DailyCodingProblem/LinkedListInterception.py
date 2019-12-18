import unittest


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


def detect_loop(target):
    slow_p = target
    fast_p = target
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return slow_p


def detect(list_a, list_b):
    if not (list_a or list_b):
        return None

    count = 1
    last = None
    pivot = list_a
    while pivot.next:
        count += 1
        pivot = pivot.next
    # circle
    pivot.next = list_a

    pivot_b = list_b
    for i in range(count):
        pivot_b = pivot_b.next

    pivot_c = list_b

    while pivot_b != pivot_c:
        pivot_b = pivot_b.next
        pivot_c = pivot_c.next

    return pivot_c


class Test(unittest.TestCase):

    def test_empty(self):
        result = detect([], [])
        self.assertIsNone(result)

    def test_case(self):
        common = Node(8, Node(10, None))
        case_a = Node(3, Node(7, common))
        case_b = Node(99, Node(1, common))
        result = detect(case_a, case_b)
        self.assertEqual(8, result.value)

    def test_case_b(self):
        common = Node(8, Node(10, None))
        case_a = common
        case_b = common
        result = detect(case_a, case_b)
        self.assertEqual(8, result.value)

if __name__ == "__main__":
    unittest.main()

