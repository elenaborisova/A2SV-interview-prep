class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return str(self.val)


# No extra space
def copyRandomList(head):
    if not head: return None

    # Insert new nodes in between old nodes
    cur = head
    while cur:
        temp = cur.next
        cur.next = Node(x=cur.val, next=temp, random=None)
        cur = temp

    # Connect the random pointers
    cur = head
    while cur:
        if cur.random:
            random_node = cur.random.next
            cur.next.random = random_node
        cur = cur.next.next

    # Delete old nodes
    cur = head
    new_head = head.next
    while cur:
        temp = cur.next.next
        copy = cur.next
        cur.next = temp
        if temp:
            copy.next = temp.next
        cur = temp

    return new_head


# Test cases:
head = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)

head.next = node1
head.random = None
node1.next = node2
node1.random = head
node2.next = node3
node2.random = node4
node3.next = node4
node3.random = node2
node4.next = None
node4.random = head

print(copyRandomList(head))
