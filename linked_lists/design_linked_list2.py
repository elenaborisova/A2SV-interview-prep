class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        cur = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = cur
            self.head = new_node
        else:
            for _ in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        cur = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.size -= 1
