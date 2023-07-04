"""2130. Maximum Twin Sum of a Linked List"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []

        while head is not None:
            nums.append(head.val)
            head = head.next

        return max(nums[i] + nums[-i - 1] for i in range(len(nums) // 2))
