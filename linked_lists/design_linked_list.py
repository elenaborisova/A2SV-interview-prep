class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i, cur = 0, self.head

        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return

        next_node = self.head
        self.head = ListNode(val)
        self.head.next = next_node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return

        cur = self.head
        while cur and cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        i, cur, prev = 0, self.head, None

        while cur:
            if i == index:
                break
            prev = cur
            cur = cur.next
            i += 1

        if i != index:
            return

        new_node = ListNode(val)
        prev.next = new_node
        new_node.next = cur

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        i, cur, prev = 0, self.head, None
        while cur:
            if i == index:
                break
            prev = cur
            cur = cur.next
            i += 1
        else:
            return

        next_node = cur.next
        if prev:
            prev.next = next_node


# Test cases:
obj = MyLinkedList()
obj.addAtTail(1)
print(obj.get(0))
