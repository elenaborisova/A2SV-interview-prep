class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def odd_even_list(head):
    if not head:
        return head

    odd = head
    even = head.next
    head_even = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = head_even
    return head


def odd_even_list2(head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)

    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None

    odd.next = dummy2.next
    return dummy1.next


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(odd_even_list(head))
