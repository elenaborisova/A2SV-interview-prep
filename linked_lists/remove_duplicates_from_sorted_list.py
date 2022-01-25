class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(1)
def delete_duplicates(head):
    cur = head

    while cur and cur.next:
        next_node = cur.next

        if cur.val == next_node.val:
            cur.next = next_node.next
        else:
            cur = cur.next

    return head


# Test cases:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(3)

print(delete_duplicates(None))
