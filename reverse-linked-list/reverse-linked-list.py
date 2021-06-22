# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head 
        stack = []
        
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
            
        curr = head
        
        while curr is not None:
            curr.val = stack.pop()
            curr = curr.next
        
        return head