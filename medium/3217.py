"""3217. Delete Nodes From Linked List Present in Array"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums_set = set(nums)

        dummy_head = ListNode(val=-1, next=head)

        prev, current, next_ = dummy_head, head, head.next

        while current:
            if current.val in nums_set:
                prev.next = next_
            else:
                prev = current

            current = next_

            if next_:
                next_ = next_.next

        return dummy_head.next
