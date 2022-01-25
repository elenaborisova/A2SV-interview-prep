class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Time: O(n + m); Space: O(1)
def merge_two_lists(list1, list2):
    dummy = cur = ListNode(0)

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next

    if list1:
        cur.next = list1
    if list2:
        cur.next = list2

    return dummy.next


# Test cases:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head2.next.next.next = ListNode(5)

print(merge_two_lists(head1, head2))
