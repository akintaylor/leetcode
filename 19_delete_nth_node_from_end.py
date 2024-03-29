# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
    on = head
    length = 1

    while on:
        length += 1
        on = on.next

    left_index = length - n - 1

    if left_index == 0:
        return head.next

    on = head

    while left_index > 1:
        left_index -= 1
        on = on.next

    on.next = on.next.next

    return head
