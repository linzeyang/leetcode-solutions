"""206. Reverse Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        current = head
        next_node = current.next
        current.next = None

        while next_node:
            prev, current, next_node = current, next_node, next_node.next
            current.next = prev

        return current
