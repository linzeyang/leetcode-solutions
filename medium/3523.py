"""3523. Make Array Non-decreasing"""

from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 1

        current_max = nums[0]

        num_of_odd = 0

        for idx in range(1, length):
            if nums[idx] >= current_max:
                current_max = nums[idx]
            else:
                num_of_odd += 1

        return length - num_of_odd
