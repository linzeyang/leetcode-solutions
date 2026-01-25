"""1877. Minimize Maximum Pair Sum in Array"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
    Biweekly Contest 53
    """

    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[idx] + nums[-idx - 1] for idx in range(len(nums) // 2))
