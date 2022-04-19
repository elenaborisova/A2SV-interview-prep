class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return str(self.val)


def max_depth(root):
    if not root:
        return 0

    if not root.children:
        return 1

    depth = 0

    for child in root.children:
        depth = max(depth, max_depth(child))

    return depth + 1


# Test cases:
root = Node(5)
node = Node(3)
root.children = [node, Node(2), Node(4)]
node2 = Node(15)
node.children = [node2, Node(17)]
node2.children = [Node(22)]

print(max_depth(root))
