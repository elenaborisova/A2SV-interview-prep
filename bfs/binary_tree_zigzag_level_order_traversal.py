from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n); Space: O(n)
def zigzag_level_order(root):
    if not root: return []

    queue = deque([root])
    res = []
    starts_left = False

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if starts_left:
            res.append(list(reversed(level)))
            starts_left = False
        else:
            res.append(level)
            starts_left = True

    return res


# Test cases:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigzag_level_order(None))
