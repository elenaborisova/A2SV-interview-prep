class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n + m); Space: O(n + m + 1)
def add_two_numbers(l1, l2):
    l1_digits = l2_digits = ''

    while l1:
        l1_digits += str(l1.val)
        l1 = l1.next

    while l2:
        l2_digits += str(l2.val)
        l2 = l2.next

    digits_sum = str(int(l1_digits[::-1]) + int(l2_digits[::-1]))[::-1]
    dummy = cur = ListNode(0)

    for d in digits_sum:
        node = ListNode(int(d))
        cur.next = node
        cur = node

    return dummy.next


# Time: (n + m); Space: O(m + n + 1)
def add_two_numbers2(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        new_val = carry % 10
        carry //= 10

        node = ListNode(new_val)
        cur.next = node
        cur = cur.next

    return dummy.next


# Test cases:
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

print(add_two_numbers2(head1, head2))
