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
        # Very slow:
        # Runtime: 77 ms, faster than 12.56% of Python3 online submissions for Reverse Linked List.
        # Memory Usage: 15.4 MB, less than 55.53% of Python3 online submissions for Reverse Linked List.
        if head is None:
            return None

        if head.next is None:
            return head

        pre = head
        node = head.next
        nex = node.next
        head.next = None

        while True:
            node.next = pre

            if nex is None:
                return node

            pre = node
            node = nex
            nex = nex.next
