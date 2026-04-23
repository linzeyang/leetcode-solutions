"""
1855. Maximum Distance Between a Pair of Values

https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

Weekly Contest 240
"""

from bisect import bisect_right
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        out: int = 0

        for idx, num in enumerate(nums1):
            if idx >= len(nums2):
                break

            if num > nums2[idx]:
                continue

            right_idx: int = bisect_right(nums2, -num, lo=idx, key=lambda x: -x) - 1
            out = max(out, right_idx - idx)

        return out
