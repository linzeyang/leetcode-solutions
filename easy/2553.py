"""
2553. Separate the Digits in an Array

https://leetcode.com/problems/separate-the-digits-in-an-array/

Biweekly Contest 97
"""

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        out: list[int] = []

        for num in nums:
            out.extend(int(char) for char in str(num))

        return out
