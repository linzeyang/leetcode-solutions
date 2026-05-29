"""
3300. Minimum Element After Replacement With Digit Sum

https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

Biweekly Contest 140
"""

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        return min(map(digit_sum, nums))
