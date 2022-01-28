import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:

    def __init__(self, head):
        self.head = head
        self.size = self.get_size()

    def get_size(self):
        size = 0
        cur = self.head

        while cur:
            size += 1
            cur = cur.next

        return size

    def getRandom(self) -> int:
        random_idx = random.randrange(0, self.size)

        cur = self.head
        for _ in range(random_idx):
            cur = cur.next
        return cur.val


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

solution = Solution(head)
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
