"""2807. Insert Greatest Common Divisors in Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = head

        while nex := node.next:
            node.next = ListNode(val=self._get_gcd(node.val, nex.val), next=nex)
            node = nex

        return head

    def _get_gcd(self, val1, val2):
        while val2:
            val1, val2 = val2, val1 % val2

        return val1
