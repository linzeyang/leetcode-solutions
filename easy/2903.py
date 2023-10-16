"""2903. Find Indices With Index and Value Difference I"""

from typing import List


class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        for idx in range(len(nums) - indexDifference):
            for jdx in range(idx + indexDifference, len(nums)):
                if abs(nums[idx] - nums[jdx]) >= valueDifference:
                    return [idx, jdx]

        return [-1, -1]
