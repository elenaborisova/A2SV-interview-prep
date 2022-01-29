class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(1)
def remove_elements(head, val):
    dummy = prev = ListNode(0, head)
    cur = head

    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next


# Test cases:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(1)

print(remove_elements(head, 1))
