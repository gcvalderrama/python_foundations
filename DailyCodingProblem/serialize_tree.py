import unittest
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(current, state):
    if not state:
        return

    while state:
        c = state.popleft()

        if c == "(":
            current.left = Node("")
            build(current.left, state)
        elif c == "[":
            current.right = Node("")
            build(current.right, state)
        elif c == ")":
            break
        elif c == "]":
            break
        elif c == "}":
            break
        else:
            current.val += c


def deserialize(text):
    if len(text) == 0:
        return
    root = Node("")
    state = deque()
    for c in text[1:]:
        state.append(c)

    build(root, state)
    return root


def in_order(node, result, open, close):
    if not node:
        return
    result.append(open)
    result.append(node.val)
    in_order(node.left, result, "(", ")")
    in_order(node.right, result, "[", "]")
    result.append(close)


def serialize(node):
    result = list()
    in_order(node, result, "{", "}")

    return "".join(result)


class Test(unittest.TestCase):

    def test_case(self):
        node = Node('root',
                    Node('A',
                         Node('AA')),
                    Node('B'))
        result = serialize(node)
        root = deserialize(result)
        two = serialize(root)
        self.assertEqual(result, two)
