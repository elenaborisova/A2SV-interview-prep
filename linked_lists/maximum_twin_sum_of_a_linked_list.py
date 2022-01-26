class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(n)
def pair_sum(head):
    stack = []
    max_sum = 0

    slow = fast = head
    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    while slow:
        one = stack.pop().val
        two = slow.val
        max_sum = max(max_sum, (one + two))
        slow = slow.next

    return max_sum


# Time: O(n); Space: O(1)
def pair_sum2(head):
    # Find middle
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
    head2 = prev

    # Find max sum
    max_sum = 0
    one, two = head, head2
    while one and two:
        max_sum = max(max_sum, (one.val + two.val))
        one = one.next
        two = two.next

    return max_sum


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(pair_sum2(head))
