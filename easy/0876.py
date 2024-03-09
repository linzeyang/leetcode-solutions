"""876. Middle of the Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set: set[ListNode] = set()
        node = head

        while node:
            if node not in node_set:
                node_set.add(node)
                node = node.next
            else:
                return True

        return False
