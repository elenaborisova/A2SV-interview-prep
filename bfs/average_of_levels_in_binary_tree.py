from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root):
    queue = deque()
    queue.append(root)
    res = []

    while queue:
        curr_sum = count = 0

        for _ in range(len(queue)):
            curr_node = queue.popleft()
            curr_sum += curr_node.val
            count += 1

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        if count:
            res.append(curr_sum / count)

    return res


# Test cases:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(average_of_levels(root))