"""82. Remove Duplicates from Sorted List II"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        existing = {}

        node = head

        while node:
            if node.val not in existing:
                existing[node.val] = 1
            else:
                existing[node.val] += 1

            node = node.next

        head = cur = None

        for k, v in existing.items():
            if v == 1:
                if not head:
                    head = ListNode(k)
                    cur = head
                else:
                    cur.next = ListNode(k)
                    cur = cur.next

        return head
