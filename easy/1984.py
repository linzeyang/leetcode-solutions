"""1984. Minimum Difference Between Highest and Lowest of K Scores"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
    Weekly Contest 256
    """

    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        return min(
            (nums[idx + k - 1] - nums[idx] for idx in range(len(nums) - k + 1)),
            default=0,
        )
