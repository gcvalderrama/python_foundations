from collections import deque



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    nodel1 = l1
    nodel2 = l2
    result = None
    pivot = None
    c = 0
    while nodel1 or nodel2:
        s = 0
        if nodel1 and nodel2:
            s = nodel1.val + nodel2.val + c
            nodel1 = nodel1.next
            nodel2 = nodel2.next
        elif nodel1:
            s = nodel1.val + c
            nodel1 = nodel1.next
        elif nodel2:
            s = nodel2.val + c
            nodel2 = nodel2.next

        if s > 9:
            c = s // 10
            s = s - 10
        else:
            c = 0

        if not pivot:
            result = ListNode(s)
            pivot = result
        else:
            node = ListNode(s)
            pivot.next = node
            pivot = node

    if c:
        pivot.next = ListNode(c)

    return result


def generate(inp1):
    root1 = ListNode(inp1[0])
    n1 = root1
    for i in inp1[1:]:
        t = ListNode(i)
        n1.next = t
        n1 = t
    return root1

if __name__ == '__main__':
    print(addTwoNumbers(generate([1]), generate([9, 9])))

