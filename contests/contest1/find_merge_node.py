class SinglyLinkedListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def findMergeNode(head1, head2):
    ll1_nodes = []

    while head1:
        ll1_nodes.append(head1)
        head1 = head1.next

    while head2:
        if head2 in ll1_nodes:
            return head2
        head2 = head2.next


# Test cases:
head1 = SinglyLinkedListNode(0)
head1.next = SinglyLinkedListNode(1)
node = SinglyLinkedListNode(2)
head1.next.next = node

head2 = SinglyLinkedListNode(5)
head2.next = node

print(findMergeNode(head1, head2))
