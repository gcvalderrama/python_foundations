class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return None

    n_a = headA
    n_b = headB

    while n_a.val != n_b.val:
        n_a = headB if n_a is None else n_a.next
        n_b = headA if n_b is None else n_b.next

    return n_a

def generate(inp1):
    root1 = ListNode(inp1[0])
    n1 = root1
    for i in inp1[1:]:
        t = ListNode(i)
        n1.next = t
        n1 = t
    return root1

if __name__ == '__main__':
    inp1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    inp2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    root1 = generate(inp1)
    root2 = generate(inp2)
    getIntersectionNode(root1, root2)

