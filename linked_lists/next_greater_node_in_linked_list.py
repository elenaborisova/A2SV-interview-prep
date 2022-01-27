class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Brute Force; Time: O(n^2); Space: O(n)
def next_larger_nodes(head):
    res = []
    slow = head

    while slow:
        fast = slow.next

        while fast:
            if fast.val > slow.val:
                res.append(fast.val)
                break
            fast = fast.next
        else:
            res.append(0)
        slow = slow.next

    return res


# Using Stack; Time: O(n); Space: O(n)
def next_larger_nodes2(head):
    stack = [head.val]
    res = [0]
    cur = head.next

    while cur:
        count = 0

        while stack and cur.val > stack[-1]:
            if res[-1 - count] == 0:
                res[-1 - count] = cur.val
                stack.pop()
            count += 1

        stack.append(cur.val)
        res.append(0)
        cur = cur.next

    return res


# Better implementation
def next_larger_nodes3(head):
    stack, res, pos = [], [], 0

    while head:
        res.append(0)

        while stack and head.val > stack[-1][1]:
            idx, _ = stack.pop()
            res[idx] = head.val

        stack.append((pos, head.val))
        head = head.next
        pos += 1

    return res


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(5)

print(next_larger_nodes3(head))
