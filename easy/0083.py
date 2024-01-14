"""83. Remove Duplicates from Sorted List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node, prev, nex = head, head, head.next

        while nex:
            if node.val != nex.val:
                node.next = nex
                node = nex
            prev = nex
            nex = nex.next

        if node.val == prev.val:
            node.next = None

        return head
