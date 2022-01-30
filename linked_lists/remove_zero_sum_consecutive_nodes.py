class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def remove_zero_sum_sublists(head):
    dummy = ListNode(0, head)
    prefix = 0
    d = {0: dummy}

    cur = head
    while cur:
        prefix += cur.val
        d[prefix] = cur
        cur = cur.next

    cur, prefix = dummy, 0
    while cur:
        prefix += cur.val
        cur.next = d[prefix].next
        cur = cur.next

    return dummy.next


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)

print(remove_zero_sum_sublists(head))