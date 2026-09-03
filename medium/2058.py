"""
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

Weekly Contest 265
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        out: list[int] = [-1, -1]

        if not head or not head.next:
            return out

        first_idx: int = -1
        last_idx: int = -1
        current_idx: int = 1
        prev_val: int = head.val

        min_distance: int = 100_000

        current: ListNode = head.next

        while current.next:
            if (current.val > prev_val and current.val > current.next.val) or (
                current.val < prev_val and current.val < current.next.val
            ):
                if first_idx == -1:
                    first_idx = current_idx
                else:
                    min_distance = min(min_distance, current_idx - last_idx)

                last_idx = current_idx

            prev_val = current.val
            current_idx += 1
            current = current.next

        if last_idx > first_idx > -1:
            out[0] = min_distance
            out[1] = last_idx - first_idx

        return out
