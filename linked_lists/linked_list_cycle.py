class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(1)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Test cases:
head = ListNode(3)
node = ListNode(2)
head.next = node
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next = node

print(has_cycle(head))
