"""747. Largest Number At Least Twice of Others"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_num_idx = -1

        for idx, num in enumerate(nums):
            if num == max_num:
                max_num_idx = idx
            elif max_num < 2 * num:
                return -1

        return max_num_idx
