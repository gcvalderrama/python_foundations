import unittest
from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def path_to_x(node: Node, x):
    if not node:
        return None
    if node.value == x:
        stack = deque()
        stack.append(x)
        return stack

    left_path = path_to_x(node.left, x)
    if left_path:
        left_path.append(node)
        return left_path

    right_path = path_to_x(node.right, x)
    if right_path:
        right_path.append(node)
        return right_path

    return None


def lca(root, j, k):
    path_to_j = path_to_x(root, j)
    path_to_k = path_to_x(root, k)
    if not path_to_j or not path_to_k:
        return None
    lca_result = None
    while path_to_j and path_to_k:
        j_pop = path_to_j.pop()
        k_pop = path_to_k.pop()
        if j_pop == k_pop:
            lca_result = j_pop
        else:
            break
    return lca_result


class Test(unittest.TestCase):

    def test_case_a(self):
        root = Node(5)
        root.right = Node(4)
        root.right.right = Node(2)
        root.right.left = Node(9)
        root.left = Node(1)
        root.left.left = Node(3)
        root.left.right = Node(8)
        root.left.left.left = Node(6)
        root.left.left.right = Node(7)

        result = lca(root, 8, 7)
        self.assertTrue(1, result)




