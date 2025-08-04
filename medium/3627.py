"""3627. Maximum Median Sum of Subsequences of Size 3"""

from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        length = len(nums)

        nums.sort(reverse=True)

        return sum(nums[idx] for idx in range(1, length // 3 * 2 + 1, 2))
