"""724. Find Pivot Index"""

# This problem is the same as 1991

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = sum(nums[1:])

        for idx, num in enumerate(nums):
            if left == right:
                return idx

            if idx == len(nums) - 1:
                break

            left += num
            right -= nums[idx + 1]

        return -1
