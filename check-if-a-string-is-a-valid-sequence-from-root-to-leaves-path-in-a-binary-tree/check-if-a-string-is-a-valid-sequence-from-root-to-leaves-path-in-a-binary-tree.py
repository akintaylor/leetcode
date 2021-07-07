# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        node = root
        pointer = 0
        
        return self.recursion(node, pointer, arr)
    
    def recursion(self, node, pointer, arr):
        if node == None or node.val != arr[pointer]:
            return False
        
        if pointer == len(arr) - 1:
            if node.left or node.right:
                return False
            
            return True
        
        return self.recursion(node.left, pointer + 1, arr) or self.recursion(node.right, pointer + 1, arr)
        
    

        
        
                    
                