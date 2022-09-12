"""
141. Linked List Cycle
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        temp = set({head})
        node = head.next

        while node is not None:
            if node in temp:
                return True
            temp.add(node)
            node = node.next

        return False
