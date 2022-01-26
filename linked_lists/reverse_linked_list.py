class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def reverse_list(head):
    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    head = prev

    return head


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(reverse_list(head))
