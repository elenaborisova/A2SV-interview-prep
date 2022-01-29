import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __repr__(self):
        return str(self.val)


# MinHeap; Time: O(n log k); Space: O(k)
def merge_k_lists(lists):
    min_heap = []
    for l in lists:
        if l:
            heapq.heappush(min_heap, (l.val, l))

    dummy = cur = ListNode(0)
    while cur and min_heap:
        node = heapq.heappop(min_heap)[1]
        cur.next = node
        cur = cur.next

        if node and node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy.next


# Divide and Conquer (Merge Sort) solution; Time: O(n log k); Space: O(log k)
def merge_k_lists2(lists):
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_lists2(lists[:mid])
    right = merge_k_lists2(lists[mid:])

    return merge(left, right)


def merge(l, r):
    dummy = p = ListNode()

    while l and r:
        if l.val < r.val:
            p.next = l
            l = l.next
        else:
            p.next = r
            r = r.next
        p = p.next

    p.next = l or r

    return dummy.next


# Test cases
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

print(merge_k_lists([head, head2, head3]))
