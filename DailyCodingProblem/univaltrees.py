# https://www.dailycodingproblem.com/blog/unival-trees/
import unittest

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None


def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False

def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right


class Test(unittest.TestCase):
    def test_case(self):
        pass
        

