"""2487. Remove Nodes From Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        if not head.next:
            return head

        while head.next and head.val < head.next.val:
            head = head.next

        sub_head = self.removeNodes(head.next)

        if not sub_head:
            return head

        if head.val >= sub_head.val:
            head.next = sub_head
        else:
            head = sub_head

        return head
