# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        on = head
        length = 0
        
        while on:
            length += 1
            on = on.next

        left_index = length - n
        if left_index == 0:
            return head.next
        
        on = head
        while left_index > 1:
            left_index -= 1
            on = on.next
            
        on.next = on.next.next
        return head
