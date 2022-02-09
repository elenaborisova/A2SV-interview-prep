class SinglyLinkedListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def removeDuplicates(llist):
    head = llist
    dummy = SinglyLinkedListNode(0, head)
    cur = head

    while cur:
        if cur.next and cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


# Test cases:
head = SinglyLinkedListNode()
# head.next = SinglyLinkedListNode(2)
# head.next.next = SinglyLinkedListNode(3)
# head.next.next.next = SinglyLinkedListNode(3)
# head.next.next.next.next = SinglyLinkedListNode(4)
# head.next.next.next.next.next = SinglyLinkedListNode(3)
# head.next.next.next.next.next.next = SinglyLinkedListNode(3)

print(removeDuplicates(None))