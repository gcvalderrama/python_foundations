
class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)

def nth_from_last(head, n):
    left = head
    right = head
    for i in range(n):
        if right is None:
            return None
        right = right.child
    while right:
        right = right.child
        left = left.child
    return left

def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)

if __name__ == "__main__":
    current = Node(1)
    for i in range(2, 8):
        current = Node(i, current)
    head = current
    print(linked_list_to_string(head))
    # 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
    # 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
    current2 = Node(4)
    for i in range(3, 0, -1):
        current2 = Node(i, current2)
    head2 = current2
    # head2 = 1 -> 2 -> 3 -> 4 -> (None)
    print("#####")
    print(nth_from_last(head, 1))
    # nth_from_last(head, 1) should return 1.
    print("#####")
    print(nth_from_last(head, 5))
    # nth_from_last(head, 5) should return 5.

    print("#####")
    print(nth_from_last(head2, 2))
    # nth_from_last(head2, 2) should return 3.
    print("#####")
    print(nth_from_last(head2, 4))
    # nth_from_last(head2, 4) should return 1.
    print("#####")
    print(nth_from_last(head2, 5))
    # nth_from_last(head2, 5) should return None.
    print("#####")
    print(nth_from_last(None, 1))
    # nth_from_last(None, 1) should return None.
