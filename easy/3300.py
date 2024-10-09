"""3300. Minimum Element After Replacement With Digit Sum"""

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        out = digit_sum(nums[0])

        for idx in range(1, len(nums)):
            if (summ := digit_sum(nums[idx])) < out:
                out = summ

        return out
