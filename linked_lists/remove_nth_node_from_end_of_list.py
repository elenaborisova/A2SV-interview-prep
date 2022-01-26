class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(1)
def remove_nth_from_end(head, n):
    slow = fast = head

    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next
    return head


def remove_nth_from_end2(head, n):
    dummy = ListNode(0, head)  # dummy points to head
    slow = dummy
    fast = head

    while n > 0 and fast:
        fast = fast.next
        n -= 1

    while fast:
        slow = slow.next
        fast = fast.next

    # delete node
    slow.next = slow.next.next

    return dummy.next  # head of ll


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(remove_nth_from_end(head, 1))
