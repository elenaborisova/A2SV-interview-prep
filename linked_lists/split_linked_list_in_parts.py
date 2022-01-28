class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def get_size(head):
    size, cur = 0, head

    while cur:
        size += 1
        cur = cur.next

    return size


# Time: O(n + k); Space: O(k)
def split_list_to_parts(head, k):
    size = get_size(head)
    parts = size // k
    rem = size % k

    res, cur = [], head
    while cur:
        part = []

        for _ in range(parts):
            part.append(cur)
            cur = cur.next

        if rem:
            part.append(cur)
            cur = cur.next
            rem -= 1

        part[-1].next = None
        res.append(part[0])

    while len(res) < k:
        res.append(None)

    return res


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)

print(split_list_to_parts(head, 3))
