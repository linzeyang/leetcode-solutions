"""
203. Remove Linked List Elements
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Using recursion
class SolutionRecursion:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Very slow:
        # Runtime: 202 ms, faster than 5.08% of Python3 online submissions for Remove Linked List Elements.
        # Memory Usage: 29 MB, less than 5.75% of Python3 online submissions for Remove Linked List Elements.
        if head is None:
            return None

        if head.val != val:
            head.next = self.removeElements(head=head.next, val=val)
            return head

        return self.removeElements(head=head.next, val=val)


# Using iteration
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Very slow:
        # Runtime: 148 ms, faster than 12.35% of Python3 online submissions for Remove Linked List Elements.
        # Memory Usage: 17.8 MB, less than 39.03% of Python3 online submissions for Remove Linked List
        if not head:
            return head

        if head.val == val:
            node = head.next
            while True:
                if node is None:
                    return
                if node.val != val:
                    head = node
                    break
                node = node.next

        node = head

        while True:
            if node.next is None:
                return head
            if node.next.val != val:
                node = node.next
                continue

            nex = node.next

            while True:
                if nex.next is None:
                    node.next = None
                    return head
                if nex.next.val == val:
                    nex = nex.next
                    continue

                node.next = nex.next
                node = nex.next
                break
