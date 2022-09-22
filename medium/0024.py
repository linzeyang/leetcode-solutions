"""
24. Swap Nodes in Pairs
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Runtime: 33 ms, faster than 92.58% of Python3 online submissions for Swap Nodes in Pairs.
        # Memory Usage: 13.8 MB, less than 64.64% of Python3 online submissions for Swap Nodes in Pairs.
        if head is None or head.next is None:
            return head

        nodea, nodeb = head, head.next
        nodea.next = nodeb.next
        nodeb.next = nodea
        head = nodeb

        while nodea.next is not None and nodea.next.next is not None:
            prev = nodea
            nodea, nodeb = nodea.next, nodea.next.next
            nodea.next = nodeb.next
            nodeb.next = nodea
            prev.next = nodeb

        return head
