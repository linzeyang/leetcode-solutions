"""
83. Remove Duplicates from Sorted List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Very slow:
        # Runtime: 88 ms, faster than 13.15% of Python3 online submissions for Remove Duplicates from Sorted List.
        # Memory Usage: 14 MB, less than 30.07% of Python3 online submissions for Remove Duplicates from Sorted List.
        if head is None:
            return

        base: int = head.val
        pre_pointer = head
        pointer: ListNode = head.next

        while pointer is not None:
            val = pointer.val

            if val == base:
                pre_pointer.next = pointer.next
            else:
                pre_pointer = pointer
                base = val

            pointer = pointer.next

        return head
