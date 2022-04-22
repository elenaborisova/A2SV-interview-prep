class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def lca_deepest_leaves(root):
    lca, max_depth = None, 0

    def dfs(node, depth):
        nonlocal lca
        nonlocal max_depth

        max_depth = max(max_depth, depth)

        if not node:
            return depth

        left = dfs(node.left, depth + 1)
        right = dfs(node.right, depth + 1)

        if left == right == max_depth:
            lca = node

        return max(left, right)

    dfs(root, 0)
    return lca


# Test cases:
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(lca_deepest_leaves(root))
