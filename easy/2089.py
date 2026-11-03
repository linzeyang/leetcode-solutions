"""
2089. Find Target Indices After Sorting Array

https://leetcode.com/problems/find-target-indices-after-sorting-array/

Weekly Contest 269
"""

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        out: list[int] = []

        for idx, num in enumerate(sorted(nums)):
            if num == target:
                out.append(idx)
            elif out:
                break

        return out
