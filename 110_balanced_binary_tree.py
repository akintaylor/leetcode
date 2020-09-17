# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_depth(root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(get_depth(root.left), get_depth(root.right))


def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True

    left_height = get_depth(root.left)
    right_height = get_depth(root.right)
    abs_height_diff = abs(left_height - right_height)

    return abs_height_diff <= 1 and is_balanced(root.left) and \
        is_balanced(root.right)
