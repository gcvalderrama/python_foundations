import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generate(inp1):
    root1 = ListNode(inp1[0])
    n1 = root1
    for i in inp1[1:]:
        t = ListNode(i)
        n1.next = t
        n1 = t
    return root1

def mergeKLists2(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    length = len(lists)
    if length == 0:
        return []
    elif length == 1:
        return lists[0]
    elif length == 2:
        return merge2Lists(lists[0], lists[1])
    else:
        first_half = mergeKLists2(lists[:length // 2])
        second_half = mergeKLists2(lists[length // 2:])
        return merge2Lists(first_half, second_half)

def merge2Lists(l1, l2):
    dummy = tail = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        else:
            tail.next = l2
            l2 = l2.next
            tail = tail.next

    tail.next = l1 or l2

    return dummy.next

def mergeKLists(lists):
    if not lists:
        return None
    arr = []
    for eachList in lists:
        curr = eachList
        while curr:
            heapq.heappush(arr, curr.val)
            curr = curr.next
    if not arr:
            return None

    head = ListNode(heapq.heappop(arr))
    tail = head
    while arr:
        newNode = ListNode(heapq.heappop(arr))
        tail.next = newNode
        tail = newNode
    return head

if __name__ == '__main__':
    n1 = generate([1, 4, 5])
    n2 = generate([1, 3, 4])
    n3 = generate([2, 6])
    root = mergeKLists([n1, n2, n3])

