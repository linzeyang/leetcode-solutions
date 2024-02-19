"""2181. Merge Nodes in Between Zeros"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals: list[int] = []

        cur = head.next
        accumulate = 0

        while cur:
            if cur.val:
                accumulate += cur.val
            else:
                vals.append(accumulate)
                accumulate = 0

            cur = cur.next

        new_head = cur = ListNode(val=vals[0])

        for idx in range(1, len(vals)):
            node = ListNode(val=vals[idx])
            cur.next = node
            cur = node

        return new_head
