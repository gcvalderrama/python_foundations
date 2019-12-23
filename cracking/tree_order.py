import unittest


class Node:

    def __init__(self):
        self.value = None
        self.right = None
        self.left = None


def order(target):

    if not target:
        return

    order(target.left)

    print(target.value)

    order(target.right)


def pre_order(target):
    if not target:
        return

    print(target.value)

    pre_order(target.left)
    pre_order(target.right)


class Test(unittest.TestCase):

    def test_case(self):
        root = Node()
        root.value = "5"
        root.left = Node()
        root.left.value = "3"

        root.left.left = Node()
        root.left.left.value = "1"

        root.left.right = Node()
        root.left.right.value = "4"

        root.right = Node()
        root.right.value = "7"

        #  order(root)
        pre_order(root)



