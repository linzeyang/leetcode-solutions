"""86. Partition List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Very slow:
        # Runtime: 75 ms, faster than 14.23% of Python3 online submissions for Partition List.
        # Memory Usage: 14 MB, less than 30.27% of Python3 online submissions for Partition List.
        if head is None or head.next is None:
            return head

        if head.val < x:
            head_of_less = tail_of_less = head
            head_of_great = tail_of_great = None
        else:
            head_of_less = tail_of_less = None
            head_of_great = tail_of_great = head

        current = head.next

        while current is not None:
            if current.val < x:
                if not head_of_less:
                    head_of_less = tail_of_less = current
                else:
                    tail_of_less.next = current
                    tail_of_less = current
            else:
                if not head_of_great:
                    head_of_great = tail_of_great = current
                else:
                    tail_of_great.next = current
                    tail_of_great = current

            current = current.next

        if not head_of_less:
            return head_of_great

        if not head_of_great:
            return head

        tail_of_less.next = head_of_great
        tail_of_great.next = None

        return head_of_less
