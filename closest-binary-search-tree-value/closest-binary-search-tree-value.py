# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.closestValueHelper(root, target, root.val)
        
    def closestValueHelper(self, node, target, closest):
        if node is None:
            return closest

        if abs(node.val - target) < abs(closest - target):
            closest = node.val
        if target < node.val:
            return self.closestValueHelper(node.left, target, closest)
        elif target > node.val:
            return self.closestValueHelper(node.right, target, closest)
        else:
            return closest
    