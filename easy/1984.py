"""1984. Minimum Difference Between Highest and Lowest of K Scores"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums = sorted(nums)

        out = None

        for idx in range(len(nums) - k + 1):
            diff = nums[idx + k - 1] - nums[idx]

            if out is None or diff < out:
                out = diff

        return out
