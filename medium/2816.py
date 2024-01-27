"""2816. Double a Number Represented as a Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack: list[int] = []
        node = head

        while node:
            stack.append(node.val)
            node = node.next

        adv = 0
        node = None

        while stack:
            val = stack.pop() * 2 + adv
            adv, val = divmod(val, 10)
            node = ListNode(val, node)

        if adv:
            node = ListNode(adv, node)

        return node
