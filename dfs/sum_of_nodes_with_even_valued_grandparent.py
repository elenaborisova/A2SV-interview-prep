class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(height)
def sum_even_grandparents(root):
    def dfs(grandparent, parent, node):
        nonlocal total_sum

        if not node:
            return

        if grandparent and grandparent.val % 2 == 0:
            total_sum += node.val

        if node.left:
            dfs(parent, node, node.left)

        if node.right:
            dfs(parent, node, node.right)

    total_sum = 0
    dfs(None, None, root)

    return total_sum


# Test cases:
root = TreeNode(6)
root.left = TreeNode(7)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(9)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)

root.right = TreeNode(8)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(5)

print(sum_even_grandparents(root))




