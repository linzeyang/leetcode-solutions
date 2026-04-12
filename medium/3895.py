"""
3895. Count Digit Appearances

https://leetcode.com/problems/count-digit-appearances/

Biweekly Contest 180
"""


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return sum(str(num).count(str(digit)) for num in nums)
