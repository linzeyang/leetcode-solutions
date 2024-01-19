"""24. Swap Nodes in Pairs"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
