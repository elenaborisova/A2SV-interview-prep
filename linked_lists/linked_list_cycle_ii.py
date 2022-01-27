class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def detect_cycle(head):
    # Find meeting point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    # Find beginning of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Test cases:
head = ListNode(3)
node = ListNode(2)
head.next = node
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = node

print(detect_cycle(head))
