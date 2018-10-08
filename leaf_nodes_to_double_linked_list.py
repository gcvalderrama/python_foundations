# https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Main function which extracts all leaves from given Binary Tree.
# The function returns new root of Binary Tree (Note that
# root may change if Binary Tree has only one node).
# The function also sets *head_ref as head of doubly linked list.
# left pointer of tree is used as prev in DLL
# and right pointer is used as next
def extractLeafList(root):
    # Base Case
    if root is None:
        return None

    if root.left is None and root.right is None:
        # This node is going to be added to doubly linked
        # list of leaves, set pointer of this node as
        # previous head of DLL. We don't need to set left
        # pointer as left is already None
        root.right = extractLeafList.head

        # Change the left pointer of previous head
        if extractLeafList.head is not None:
            extractLeafList.head.left = root

            # Change head of linked list
        extractLeafList.head = root

        return None  # Return new root

    # Recur for right and left subtrees
    root.right = extractLeafList(root.right)
    root.left = extractLeafList(root.left)

    return root


# Utility function for printing tree in InOrder
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)


def printList(head):
    while (head):
        if head.data is not None:
            print(head.data)
        head = head.right


def BTToDLLUtil(root):
    """This is a utility function to convert the binary tree to doubly linked list. Most of the core task
    is done by this function."""
    if root is None:
        return root

    # Convert left subtree and link to root
    if root.left:

        # Convert the left subtree
        left = BTToDLLUtil(root.left)

        # Find in order predecessor, After this loop, left will point to the in order predecessor of root
        while left.right:
            left = left.right

        # Make root as next of predecessor
        left.right = root

        # Make predecessor as
        # previous of root
        root.left = left

    # Convert the right subtree
    # and link to root
    if root.right:

        # Convert the right subtree
        right = BTToDLLUtil(root.right)

        # Find inorder successor, After
        # this loop, right will point to
        # the inorder successor of root
        while right.left:
            right = right.left

            # Make root as previous
        # of successor
        right.left = root

        # Make successor as
        # next of root
        root.right = right

    return root


def BTToDLL(root):
    if root is None:
        return root

    # Convert to doubly linked
    # list using BLLToDLLUtil
    root = BTToDLLUtil(root)

    # We need pointer to left most
    # node which is head of the
    # constructed Doubly Linked list
    while root.left:
        root = root.left

    return root


def print_list(head):
    """Function to print the given
       doubly linked list"""
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = BTToDLL(root)
    print_list(head)

# This code is contributed
# by viveksyngh


if __name__ == "__maina__":
    # Driver program to test above function
    extractLeafList.head = Node(None)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    print("Inorder traversal of given tree is:")
    printInorder(root)

    root = extractLeafList(root)

    print("\nExtract Double Linked List is:")
    printList(extractLeafList.head)

    print("\nInorder traversal of modified tree is:")
    printInorder(root)

