class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(1)
def swap_pairs(head):
    dummy = prev = ListNode(0, head)
    cur = head

    while cur and cur.next:
        next_node = cur.next
        cur.next = next_node.next
        next_node.next = cur
        prev.next = next_node

        prev = cur
        cur = cur.next

    return dummy.next


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(swap_pairs(head))



