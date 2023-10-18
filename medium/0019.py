"""19. Remove Nth Node From End of List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n - 1):
            fast = fast.next

        if not fast.next:
            return head.next

        prev, slow, fast = slow, slow.next, fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next

        return head
