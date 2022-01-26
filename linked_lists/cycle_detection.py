class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1

    return 0


# Test cases:
head = ListNode(3)
node = ListNode(2)
head.next = node
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next = node

print(has_cycle(head))
