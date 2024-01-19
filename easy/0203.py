"""203. Remove Linked List Elements"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Using recursion
class SolutionRecursion:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        if head.val != val:
            head.next = self.removeElements(head=head.next, val=val)
            return head

        return self.removeElements(head=head.next, val=val)


# Using iteration
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        if not head:
            return

        prev, current = head, head.next

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current

            current = current.next

        return head
