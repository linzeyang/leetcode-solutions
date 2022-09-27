"""
206. Reverse Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Slow:
        # Runtime: 73 ms, faster than 24.32% of Python3 online submissions for Reverse Linked List.
        # Memory Usage: 15.6 MB, less than 27.64% of Python3 online submissions for Reverse Linked List.
        if head is None:
            return head

        pre, node = None, head

        while node is not None:
            nex = node.next
            node.next = pre
            pre = node
            node = nex

        return pre
