class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# Time: O(n); Space: O(n)
def find_tilt(root):
    total_tilt = 0

    def dfs(root):
        nonlocal total_tilt

        if not root:
            return 0

        left_sum = dfs(root.left)
        right_sum = dfs(root.right)
        tilt = abs(left_sum - right_sum)
        total_tilt += tilt

        return left_sum + right_sum + root.val

    dfs(root)
    return total_tilt


# Test cases:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(find_tilt(root))