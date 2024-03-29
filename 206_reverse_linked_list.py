# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#  iteratively
def reverse_list(head: ListNode) -> ListNode:
    on = head
    prev = None

    while on:
        temp = on.next
        on.next = prev
        prev = on
        on = temp

    return prev


# recursively
def reverse_list(on: ListNode, prev=None) -> ListNode:
    if on is None:
        return prev

    temp = on.next
    on.next = prev

    return reverse_list(temp, on)
