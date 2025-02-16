"""3452. Sum of Good Numbers"""

from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        out = 0

        for idx, num in enumerate(nums):
            left = nums[idx - k] if idx - k >= 0 else 0
            right = nums[idx + k] if idx + k < len(nums) else 0

            if num > left and num > right:
                out += num

        return out
