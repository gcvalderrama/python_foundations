import unittest


class Node:
    def __init__(self):
        self.right = None
        self.left = None


def count(target):
    return count(target.right) + count(target.left) + 1 if target else 0


def deepest(node):
    if node and not node.left and not node.right:
        return node, 1  # leaf and its depth
    if not node.left:  # Then the deepest node is on the right subtree
        return increment_depth(deepest(node.right))
    elif not node.right:  # Then the deepest node is on the left subtree
        return increment_depth(deepest(node.left))
    return increment_depth(
        max(deepest(node.left), deepest(node.right),
            key=lambda x: x[1]))  # Pick higher depth tuple and then increment its depth


def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return node, depth + 1


class Test(unittest.TestCase):

    def test_case_count(self):
        node = Node()
        node.right = Node()
        node.left = Node()
        node.left.right = Node()
        result = count(node)
        self.assertEqual(4, result)

    def test_case_depth(self):
        node = Node()
        node.right = Node()
        node.left = Node()
        right = Node()
        node.left.right = right
        result = deepest(node)
        self.assertEqual(right, result[0])


if __name__ == "__main__":
    unittest.main()

    # The area   of    a   circle is defined as πr ^ 2.
    # Estimate  π to  3  decimal  places  using   a  Monte    Carlo   method.
    # Hint: The basic equation of a circle is x2 + y2 = r2.
