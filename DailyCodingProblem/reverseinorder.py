import unittest
import math
from collections import deque


class Node:

    def __init__(self, value=None, left=None, right=None):
        self.value = None
        self.left = left
        self.right = right


def pre_order(node: Node, result: list):
    if not node:
        return

    result.append(node.value)
    pre_order(node.left, result)
    pre_order(node.right, result)


def in_order(node: Node, result: list):
    if not node:
        return

    in_order(node.left, result)
    result.append(node.value)
    in_order(node.right, result)


def recursive_pre_order(root: Node, queue: deque, height: int):
    if not queue:
        return

    root.value = queue.popleft()

    if height > 1:
        root.left = Node()
        root.right = Node()
        recursive_pre_order(root.left, queue, height - 1)
        recursive_pre_order(root.right, queue, height - 1)


def recursive_in_order(root: Node, queue: deque, height: int):
    if not queue:
        return

    if height > 1:
        root.left = Node()
        recursive_in_order(root.left, queue, height - 1)

    root.value = queue.popleft()

    if height > 1:
        root.right = Node()
        recursive_in_order(root.right, queue, height - 1)


def reverse_pre_order(target: list):
    h = int(math.log(len(target) + 1, 2))
    queue = deque(target)
    root = Node()
    recursive_pre_order(root, queue, h)
    return root


def reverse_in_order(target: list):
    h = int(math.log(len(target) + 1, 2))
    queue = deque(target)
    root = Node()
    recursive_in_order(root, queue, h)
    return root


class Test(unittest.TestCase):

    def test(self):
        target = ["a", "b", "d", "e", "c", "f", "g"]
        root = reverse_pre_order(target)
        result = list()
        pre_order(root, result)
        self.assertEqual("".join(result), "abdecfg")

    def test_in_order(self):
        target = ["d", "b", "e", "a", "f", "c", "g"]
        root = reverse_in_order(target)
        result = list()
        in_order(root, result)
        self.assertEqual("".join(result), "dbeafcg")


if __name__ == '__main__':
    unittest.main()


