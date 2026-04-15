"""
1848. Minimum Distance to the Target Element

https://leetcode.com/problems/minimum-distance-to-the-target-element/

Weekly Contest 239
"""

from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        out: int = len(nums)

        for idx, num in enumerate(nums):
            if num == target:
                out = min(out, abs(idx - start))

        return out
