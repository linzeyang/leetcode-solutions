""""""

from math import ceil
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        count = 0

        node = head

        while node.next is not None:
            count += 1
            node = node.next

        steps = ceil(count / 2)

        node = head

        for _ in range(steps):
            node = node.next

        return node
