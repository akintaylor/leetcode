# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1 - DFS
def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


# Solution 2 - BFS
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    queue = [root]
    depth = 0

    while queue:
        size = len(queue)
        depth += 1
        while size > 0:
            item = queue.pop(0)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            size -= 1
    return depth
