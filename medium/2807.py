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
        if not head:
            return head

        curr = head

        while nex := curr.next:
            curr.next = ListNode(val=self._gcd(curr.val, nex.val), next=nex)
            curr = nex

        return head

    @staticmethod
    def _gcd(num1: int, num2: int) -> int:
        if num1 < num2:
            num1, num2 = num2, num1

        while num1 % num2:
            num1, num2 = num2, num1 - num2

            if num1 < num2:
                num1, num2 = num2, num1

        return num2
