class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# DFS recursive
def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right and root.val == target_sum:
        return True

    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


# DFS with stack
def has_path_sum2(root, target_sum):
    stack = [(root, target_sum)]

    while stack:
        node, value = stack.pop()

        if node:
            if not node.left and not node.right and node.val == value:
                return True

            stack.append((node.right, value - node.val))
            stack.append((node.left, value - node.val))

    return False


# Test cases:
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(has_path_sum(root, 22))
