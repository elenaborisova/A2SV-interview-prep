class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return str(self.val)


def copyRandomList(head):
    d = {}

    cur = head
    while cur:
        d[cur] = Node(cur.val)
        cur = cur.next
    d[None] = None

    for old, new in d.items():
        if old:
            new.next = d[old.next]
            new.random = d[old.random]

    return d[head]


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

# head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
