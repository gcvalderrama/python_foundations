import unittest


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def post_order(node: Node, temp: list):
    if not node:
        return
    temp.append("(")
    post_order(node.left, temp)
    temp.append(node.value)
    post_order(node.right, temp)
    temp.append(")")


def evaluate(root: Node):
    temp = list()
    post_order(root, temp)
    target = "".join(temp)
    print(target)
    return eval(target)


class Test(unittest.TestCase):

    def test_initial(self):
        left = Node("+", Node("3"), Node("2"))
        right = Node("+", Node("4"), Node("5"))
        root = Node("*", left, right)
        result = evaluate(root)
        self.assertEqual(45, result)

