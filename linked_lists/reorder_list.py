class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def reorder_list(head):
    # Find middle element
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev, cur = None, slow
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    # Reorder list
    first, second = head, prev
    while second.next:
        next_node = first.next
        first.next = second
        first = next_node

        next_node = second.next
        second.next = first
        second = next_node


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)

print(reorder_list(head))
