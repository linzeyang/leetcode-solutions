"""
19. Remove Nth Node From End of List
"""
from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Very slow:
        # Runtime: 73 ms, faster than 10.14% of Python3 online submissions for Remove Nth Node From End of List.
        # Memory Usage: 13.9 MB, less than 70.36% of Python3 online submissions for Remove Nth Node From End of List.
        if head is None or head.next is None:
            return

        queue = deque(maxlen=n + 1)
        node = head

        while node is not None:
            queue.append(node)
            node = node.next

        if n == 1:
            queue[-2].next = None
            return head

        if len(queue) < n + 1:
            queue[0].next = None
            return queue[1]

        queue[0].next = queue[2]
        queue[1].next = None
        return head
