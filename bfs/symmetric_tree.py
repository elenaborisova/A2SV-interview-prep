from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()

            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)

        if not level == level[::-1]:
            return False

    return True


# Test cases:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
root.right.right = TreeNode(4)

print(is_symmetric(root))