"""3788. Maximum Score of a Split"""

from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        out: int | float = float("-inf")

        prefix_sum: int = sum(nums) - nums[-1]
        suffix_min: int = nums[-1]

        for idx in range(2, len(nums) + 1):
            out = max(out, prefix_sum - suffix_min)

            prefix_sum -= nums[-idx]
            suffix_min = min(nums[-idx], suffix_min)

        return int(out)
